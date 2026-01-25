from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

# Allow importing utils.py from src/ without packaging.
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from utils import ensure_ucibike_data  # noqa: E402


@st.cache_data(show_spinner=False)
def load_data(level: str) -> pd.DataFrame:
    csv_path = ensure_ucibike_data(raw_dir=ROOT / "data" / "raw", level=level)
    df = pd.read_csv(csv_path)
    df.columns = [c.strip() for c in df.columns]
    if "dteday" in df.columns:
        df["dteday"] = pd.to_datetime(df["dteday"], errors="coerce")
    if "weekday" in df.columns:
        df["is_weekend"] = df["weekday"].isin([0, 6]).astype(int)
    return df


st.set_page_config(page_title="Bike Sharing Peak Hours", layout="wide")
st.title("Bike Sharing — Peak Hours")
st.caption("Interactive view of the UCI Bike Sharing dataset.")

level = st.sidebar.selectbox("Dataset level", ["hour", "day"], index=0)
df = load_data(level)

st.metric("Rows", f"{len(df):,}")
st.metric("Columns", f"{len(df.columns):,}")

with st.expander("Preview data", expanded=False):
    st.dataframe(df.head(50))

if {"dteday", "cnt"}.issubset(df.columns) and df["dteday"].notna().any():
    daily = df.groupby("dteday", as_index=False)["cnt"].sum()
    st.subheader("Daily rentals over time")
    st.line_chart(daily, x="dteday", y="cnt")

if {"temp", "cnt"}.issubset(df.columns):
    st.subheader("Temperature vs rentals")
    st.scatter_chart(df, x="temp", y="cnt")

if {"hr", "cnt"}.issubset(df.columns):
    st.subheader("Average rentals by hour")
    avg_by_hr = df.groupby("hr", as_index=False)["cnt"].mean()
    st.line_chart(avg_by_hr, x="hr", y="cnt")

    st.subheader("Peak hours by day type")
    df = df.copy()
    if "is_weekend" not in df.columns:
        df["is_weekend"] = 0
    df["_daytype"] = np.where(df["is_weekend"] == 1, "weekend", "workingday")
    if "workingday" in df.columns:
        df.loc[(df["workingday"] == 0) & (df["is_weekend"] == 0), "_daytype"] = "non-workingday"

    peak = (
        df.groupby(["_daytype", "hr"], as_index=False)["cnt"]
        .mean()
        .rename(columns={"cnt": "avg_cnt"})
        .sort_values(["_daytype", "avg_cnt"], ascending=[True, False])
    )
    peak_top = peak.groupby("_daytype", as_index=False).head(5)
    st.dataframe(peak_top, use_container_width=True)
else:
    st.info("Hour-level charts are available when using the hour dataset.")
