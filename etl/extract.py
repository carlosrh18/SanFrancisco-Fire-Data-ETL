import requests
import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class FireIncidentExtractor:
    def __init__(self, url: str, output_path: str = "../data/fire_incidents.csv"):
        self.url = url
        self.output_path = Path(output_path)

    def download_csv(self) -> pd.DataFrame:
        logging.info(f"Downloading CSV data from {self.url}")
        try:
            df = pd.read_csv(self.url)
            logging.info(f"Downloaded {len(df)} records.")
            return df
        except Exception as e:
            logging.error(f"Failed to download or parse CSV: {e}")
            raise

    def save_to_csv(self, df: pd.DataFrame):
        try:
            self.output_path.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(self.output_path, index=False)
            logging.info(f"Saved data to {self.output_path}")
        except Exception as e:
            logging.error(f"Failed to save CSV: {e}")
            raise

    def run(self):
        df = self.download_csv()
        self.save_to_csv(df)


if __name__ == "__main__":
    extractor = FireIncidentExtractor(
        url="https://data.sfgov.org/api/views/wr8u-xric/rows.csv?accessType=DOWNLOAD"
    )
    extractor.run()
