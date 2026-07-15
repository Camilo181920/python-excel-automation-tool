import pandas as pd

from src.utils import setup_logger
from src.validator import validate_data

logger = setup_logger()


def process_excel(input_file):

    logger.info(f"Reading Excel file: {input_file}")

    df = pd.read_excel(input_file)

    original_rows = len(df)

    df = validate_data(df)

    cleaned_rows = len(df)

    removed_rows = original_rows - cleaned_rows

    logger.info(f"Removed {removed_rows} invalid rows")

    df["Total"] = df["Quantity"].astype(float).mul(df["Price"].astype(float))

    return df
