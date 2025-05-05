import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv("../.env")

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

def load_data():
    df = pd.read_csv("../data/fire_incidents_clean.csv")
    df.to_sql("fire_incidents", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    load_data()