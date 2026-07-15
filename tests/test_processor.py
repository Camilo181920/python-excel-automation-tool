import pandas as pd

from src.processor import process_excel


def test_process_excel(tmp_path):

    input_file = tmp_path / "test.xlsx"

    data = {
        "Date": ["2026-01-01"],
        "Product": ["Laptop"],
        "Quantity": [2],
        "Price": [1000],
    }

    df = pd.DataFrame(data)

    df.to_excel(input_file, index=False)

    result = process_excel(input_file)

    assert len(result) == 1

    assert result.iloc[0]["Total"] == 2000
