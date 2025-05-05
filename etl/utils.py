import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

def get_engine():
    load_dotenv("../.env")
    return create_engine(
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )