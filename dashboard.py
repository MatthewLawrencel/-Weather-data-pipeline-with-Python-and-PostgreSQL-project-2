import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

st.title("🌦️ Indian Weather Dashboard")
st.write("Displays weather data loaded into PostgreSQL.")

DATABASE_URL = os.getenv("DATABASE_URL")

@st.cache_data
def load_data():
    engine = create_engine(DATABASE_URL)
    return pd.read_sql("SELECT * FROM weather_reports", engine)

df = load_data()

st.dataframe(df, use_container_width=True)

city = st.selectbox("Choose City", df["city"].unique())
filtered = df[df["city"] == city]

st.write("### City Weather Details")
st.write(filtered)

