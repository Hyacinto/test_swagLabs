#!/bin/bash
python main.py
echo "Main.py completed and CSV file generated."
echo "Running tests and generating Allure results..."
pytest tests/ --alluredir=allure-results
if [ ! -d "allure-results" ]; then
    echo "Error: Allure results directory not found. Tests might have failed."
    exit 1
fi
echo "Generating Allure report..."
allure generate allure-results -o allure-report --clean
if [ ! -d "allure-report" ]; then
    echo "Error: Allure report generation failed."
    exit 1
fi
echo "Starting Allure report on http://localhost:5050"
python3 -m http.server 5050 --directory allure-report


