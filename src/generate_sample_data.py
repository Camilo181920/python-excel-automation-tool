import os
import random
from datetime import datetime, timedelta

import pandas as pd


def create_sample_data():

    random.seed(42)

    products = {
        "Laptop": 1200,
        "Monitor": 350,
        "Keyboard": 80,
        "Mouse": 25,
        "Webcam": 95,
        "Headset": 150,
        "Dock Station": 220,
        "SSD 1TB": 140,
        "USB Hub": 45,
        "Office Chair": 420,
    }

    start_date = datetime(2026, 1, 1)

    data = []

    for _ in range(100):

        product = random.choice(list(products.keys()))

        base_price = products[product]

        price = round(
            base_price * random.uniform(0.9, 1.1),
            2
        )

        quantity = random.randint(1, 8)

        date = (
            start_date +
            timedelta(days=random.randint(0, 180))
        ).strftime("%Y-%m-%d")

        data.append(
            {
                "Date": date,
                "Product": product,
                "Quantity": quantity,
                "Price": price,
            }
        )

    # Agregar algunos registros inválidos
    data.extend(
        [
            {
                "Date": "2026-06-20",
                "Product": None,
                "Quantity": 2,
                "Price": 300,
            },
            {
                "Date": "2026-06-21",
                "Product": "Laptop",
                "Quantity": None,
                "Price": 1200,
            },
            {
                "Date": "2026-06-22",
                "Product": "Mouse",
                "Quantity": -5,
                "Price": 20,
            },
            {
                "Date": "2026-06-23",
                "Product": "Keyboard",
                "Quantity": 3,
                "Price": -50,
            },
        ]
    )

    df = pd.DataFrame(data)

    os.makedirs(
        "data/input",
        exist_ok=True
    )

    output_file = "data/input/sales.xlsx"

    df.to_excel(
        output_file,
        index=False
    )

    print(f"Sample file created: {output_file}")
    print(f"Generated records: {len(df)}")


if __name__ == "__main__":
    create_sample_data()