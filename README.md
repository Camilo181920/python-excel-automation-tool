# Excel Automation Tool

![Project Overview](screenshots/project_overview.png)

A professional Python automation solution designed to process Excel files, validate business data, generate reports, and create automated summaries.

This project demonstrates how repetitive spreadsheet workflows can be transformed into reliable automation processes that reduce manual work, improve accuracy, and save business time.

---

## Overview

Many businesses spend hours every week manually cleaning spreadsheets, validating information, and preparing reports.

This tool automates that workflow by:

- Reading Excel files automatically.
- Validating business data.
- Removing invalid records.
- Processing and transforming information.
- Generating professional Excel reports.
- Creating business summaries and charts.

---

## Features

### Excel Data Processing

- Import Excel files automatically.
- Validate required columns.
- Detect missing information.
- Remove invalid records.
- Calculate derived values.

### Data Validation

The system validates:

- Missing products.
- Empty quantities.
- Invalid prices.
- Negative values.
- Required spreadsheet structure.

### Automated Reports

The generated Excel report includes:

### Processed Data Sheet

Contains:

- Cleaned records.
- Calculated totals.
- Formatted Excel table.
- Frozen headers.
- Automatic column sizing.

### Summary Dashboard

Contains:

- Total transactions.
- Total sales.
- Average sale.
- Highest sale.
- Lowest sale.

### Visualization

Automatically generates:

- Sales by product chart.

---

# Project Structure


excel-automation-tool/

├── src/
│ ├── main.py
│ ├── generate_sample_data.py
│ ├── processor.py
│ ├── validator.py
│ ├── reporter.py
│ └── utils.py
│
├── tests/
│ ├── test_validator.py
│ └── test_processor.py
│
├── data/
│ ├── input/
│ └── output/
│
├── logs/
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore


---

# Technologies

- Python 3
- Pandas
- OpenPyXL
- Pytest
- Excel Automation
- Data Processing
- Logging

---

# Installation

Clone the repository:

git clone <repository-url>

cd excel-automation-tool

Create virtual environment:

python3 -m venv .venv

Activate environment:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

# Generate Sample Data

The project includes a script to generate sample Excel data.

Run:

python src/generate_sample_data.py

Generated file:

data/input/sales.xlsx

# Run Application

Execute:

python src/main.py \
--input data/input/sales.xlsx \
--output data/output/report.xlsx

Example:

python src/main.py --input sales.xlsx --output report.xlsx

# Output

The application generates:

data/output/report.xlsx

The Excel file contains:

Processed Data

A cleaned dataset with:

Valid records.
Calculated totals.
Professional formatting.
Summary Dashboard

Includes:

Total transactions.
Total sales.
Average transaction value.
Highest transaction.
Lowest transaction.
Sales Chart

Automatically generated visualization showing sales by product.

# Logging

Application execution logs are stored in:

logs/app.log

Example:

INFO | Reading Excel file
INFO | Removed invalid rows
INFO | Report generated successfully

# Testing

The project includes automated tests using Pytest.

Run:

pytest

Expected result:

2 passed

Tests validate:

Data cleaning rules.
Excel processing logic.
Calculation accuracy.

# Use Cases

This solution can be adapted for:

Sales report automation.
Inventory processing.
Financial spreadsheets.
Customer data cleaning.
Business reporting workflows.
Recurring Excel tasks.

# Future Improvements

Possible extensions:

Database integration.
REST API service.
Scheduled execution.
Email report delivery.
Cloud deployment.
Web dashboard.

# Skills Demonstrated
Python Automation
Excel Automation
Pandas
OpenPyXL
Data Processing
Data Validation
Report Generation
Automated Testing
Clean Code Practices

# Author

Python Automation Developer

Specialized in:

Python automation solutions.
API integrations.
Backend development.
Data processing workflows.

---

# Docker Usage

Build the Docker image:

docker compose build

Run the application:

docker compose up

The generated report will be available at:

data/output/report.xlsx