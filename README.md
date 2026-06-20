# SQL Data Validation Portfolio

![CI](https://github.com/mikerdiaz/sql-data-validation-portfolio/actions/workflows/ci.yml/badge.svg)

Data validation framework using Python, SQLite, and Pytest to demonstrate
real-world QA testing for data integrity and quality assurance.

## Tech Stack

- Python 3.13
- SQLite
- Pytest

## Project Structure

```
sql-data-validation-portfolio/

├── database/
│   └── create_db.py
├── tests/
│   └── test_data_validation.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Test Cases

- Orphan orders detection (referential integrity)
- Null/empty email validation
- Negative order amount validation
- Customer order totals with LEFT JOIN

## How to Run

```bash
python database/create_db.py
pytest tests/ -v
```

## Author

Mike Diaz – QA Automation Engineer
Vancouver, BC, Canada
github.com/mikerdiaz