import argparse

from src.processor import process_excel
from src.reporter import generate_report


def main():

    parser = argparse.ArgumentParser(description="Excel Automation Tool")

    parser.add_argument(
        "--input",
        required=True,
        help="Input Excel file",
    )

    parser.add_argument(
        "--output",
        default="data/output/report.xlsx",
        help="Generated report file",
    )

    args = parser.parse_args()

    df = process_excel(args.input)

    generate_report(
        df,
        args.output,
    )


if __name__ == "__main__":
    main()
