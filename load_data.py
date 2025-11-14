import pandas as pd
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def load_to_postgres(df):
    if df.empty:
        print("No data to load.")
        return

    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            conn.execute(text("TRUNCATE TABLE weather_reports;"))
            conn.commit()

        df.to_sql("weather_reports", engine, if_exists="append", index=False)
        print(f"Successfully loaded {len(df)} rows into PostgreSQL.")
    except Exception as e:
        print(f"Database load failed: {e}")

