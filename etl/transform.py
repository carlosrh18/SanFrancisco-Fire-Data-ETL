import pandas as pd
import logging
import os

INPUT_FILE = "../data/fire_incidents.csv"
OUTPUT_FILE = "../data/fire_incidents_clean.csv"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def transform(input_file=INPUT_FILE, output_file=OUTPUT_FILE):
    try:
        if not os.path.exists(input_file):
            logging.error(f"Input file {input_file} does not exist.")
            return
        
        logging.info(f"Reading the CSV file from {input_file}...")
        df = pd.read_csv(input_file)
        
        logging.info("Dropping duplicate rows...")
        df.drop_duplicates(subset=["Incident Number"], inplace=True)
        
        logging.info("Dropping rows with missing values in critical columns...")
        df.dropna(subset=["Incident Date", "Battalion", "Supervisor District"], inplace=True)
        
        logging.info(f"Saving the cleaned data to {output_file}...")
        df.to_csv(output_file, index=False)
        logging.info("Transformation complete.")
    except Exception as e:
        logging.error(f"An error occurred during transformation: {e}")

if __name__ == "__main__":
    transform()