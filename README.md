# Python AI Model BootCamp

This project is a hands-on learning folder for Python-based data analysis, exploratory data analysis (EDA), and basic machine learning. It includes small practice scripts, CSV datasets, and simple regression models built with `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-learn`.

## Overview

The repository is designed for learning and experimentation. It covers:

- Python basics and data structures
- Data loading and transformation with `pandas`
- Numerical operations with `numpy`
- Data visualization with `matplotlib` and `seaborn`
- Exploratory analysis of real-world style datasets
- Simple predictive modeling using linear regression and random forest regression

## Project Structure

- `numpy_practice.py` — basic NumPy array operations and numeric calculations
- `pandas_practice.py` — DataFrame creation, CSV reading, and summary statistics
- `eda_practice.py` — exploratory data analysis on land pricing data
- `eda_visual.py` — EDA visuals using histograms, scatter plots, and box plots
- `student_score_model.py` — simple linear regression model for study hours vs. scores
- `Project/land_price_predictor.py` — predictive model for land price estimation
- `sample.py` — beginner sample script
- `land_price.csv` and `land_prices.csv` — land pricing datasets
- `students_data.csv` and `study_habits.csv` — student data used in practice scripts
- `setup.sh` — sets up a virtual environment and installs required Python packages

## Setup

1. Open the project folder in a terminal.
2. Create the environment and install dependencies:

```bash
bash setup.sh
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Run any script directly:

```bash
python numpy_practice.py
python pandas_practice.py
python eda_practice.py
python eda_visual.py
python student_score_model.py
python Project/land_price_predictor.py
```

## Dependencies

The project uses the following Python libraries:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

These are installed by `setup.sh`.

## Example Learning Goals

- Understand how to read CSV files into a DataFrame
- Perform basic data cleaning and feature engineering
- Explore patterns in data using plots
- Prepare train/test data for machine learning
- Train and evaluate a regression model
- Interpret metrics such as MAE, MSE, RMSE, and R²

## Notes

This repository is intended for educational practice and experimentation. It is not a production-ready application or deployment project. Instead, it focuses on learning core Python data science and AI concepts through small, manageable examples.

## Suggested Next Steps

- Add a Jupyter Notebook for exploratory analysis
- Build a model pipeline with preprocessing and validation
- Compare several regression models
- Add documentation for each dataset and script
- Save model outputs and predictions to CSV files
