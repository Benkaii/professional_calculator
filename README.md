# Professional Calculator

## Overview
This project is a professional calculator application built in Python using object-oriented programming (OOP) principles. The calculator performs basic arithmetic operations and includes automated testing with Pytest and GitHub Actions CI/CD.

## Features
- Addition
- Subtraction
- Multiplication
- Division
- Divide-by-zero error handling
- Object-oriented design
- Automated testing with Pytest
- 100% test coverage
- Continuous Integration using GitHub Actions

## Project Structure

```text
professional_calculator/
│── .github/workflows/
│   └── python-app.yml
│── app/
│   ├── calculation/
│   ├── calculator/
│   └── operation/
│── tests/
│   ├── test_calculations.py
│   ├── test_calculator.py
│   └── test_operations.py
│── requirements.txt
│── pytest.ini
│── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Benkaii/professional_calculator.git
cd professional_calculator
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Tests

To run all tests:

```bash
pytest
```

This project includes:
- 31 passing tests
- 100% test coverage

## Technologies Used
- Python
- Pytest
- Pytest-Cov
- GitHub Actions
- Git