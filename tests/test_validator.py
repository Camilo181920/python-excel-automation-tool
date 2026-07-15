import pandas as pd

from src.validator import validate_data


def test_validate_data_removes_invalid_rows():

    data = {
        "Date": ["2026-01-01", "2026-01-02", "2026-01-03"],
        "Product": ["Laptop", None, "Mouse"],
        "Quantity": [2, 5, -1],
        "Price": [1000, 50, 20],
    }

    df = pd.DataFrame(data)

    result = validate_data(df)

    assert len(result) == 1
    assert result.iloc[0]["Product"] == "Laptop"
