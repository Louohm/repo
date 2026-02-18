# AutoInsight: Automated Data Analysis
Building AI course project

## Summary
AutoInsight is an AI-driven tool for automated CSV data analysis. It helps identify correlations and generates quick textual insights from datasets by automatically calculating means and identifying strong relationships between numeric variables. This project simplifies the initial data exploration phase for analysts and researchers.

## Data sources and AI methods
The data used in this project is provided via CSV files, such as the included 'sample_data.csv'. The AI methods involve automated correlation analysis and descriptive statistics using the Python library Pandas to find patterns and relationships within the data.

## How to use
To use AutoInsight, follow these steps:
1. Ensure you have Python and Pandas installed.
2. Place your dataset in the same folder as the script and name it 'sample_data.csv'.
3. Run the script using the command: `python ai.py`.
4. The tool will automatically output a correlation matrix and key insights directly in your terminal.

![Analysis Demo](https://tinyurl.com/elementsofaicat)

## Challenges
One challenge is handling non-numeric data or missing values, which can affect the correlation matrix. Future versions could include automated data cleaning.

## What next?
The project could be expanded to include visual charts using Matplotlib or Seaborn, and potentially use machine learning models to predict future trends based on the identified correlations.

## Acknowledgments
* Inspired by the Building AI course project.
* Built using the Pandas library for Python.
