import pandas as pd

REQUIRED_COLUMNS = ["Date", "Product", "Quantity", "Price"]


def validate_columns(df: pd.DataFrame):
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_data(df: pd.DataFrame):

    validate_columns(df)

    valid_df = df.copy()

    valid_df = valid_df.dropna(subset=["Product", "Quantity", "Price"])

    valid_df = valid_df[valid_df["Quantity"] > 0]

    valid_df = valid_df[valid_df["Price"] > 0]

    return valid_df
