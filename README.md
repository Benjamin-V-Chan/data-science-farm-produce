# data-science-farm-produce

## Project Overview

This project analyzes 80 years of Canadian farm production data to uncover trends, build forecasting models, and simulate future scenarios. Through a series of modular scripts, the workflow performs data cleaning, feature engineering, exploratory analysis, time-series forecasting, predictive modeling, and Monte Carlo simulations. Techniques include statistical preprocessing, trend analysis, regression modeling, and uncertainty quantification to provide a comprehensive view of agricultural dynamics across provinces and crop types.

## Folder Structure

```
project-root/
├── data/                   # Raw dataset files
│   └── farm_production_dataset.csv
├── scripts/                # Analysis and modeling scripts
│   ├── 01_data_preprocessing.py
│   ├── 02_feature_engineering.py
│   ├── 03_exploratory_analysis.py
│   ├── 04_time_series_forecasting.py
│   ├── 05_predictive_modeling.py
│   └── 06_scenario_simulation.py
├── outputs/                # Results and visualizations
│   ├── processed_data.csv
│   ├── features.csv
│   ├── target.csv
│   ├── correlation_matrix.csv
│   ├── figures/            # Exploratory plots
│   ├── figures/forecasts/  # Forecast plots
│   ├── forecasts.csv
│   ├── metrics.csv
│   ├── feature_importances.csv
│   └── simulations/        # Monte Carlo output folders
└── requirements.txt        # Python dependencies
```

## Usage

1. **Setup the Project:**

   ```bash
   # Clone the repository
   git clone <your-repo-url>
   cd project-root

   # Ensure Python is installed and install dependencies
   pip install -r requirements.txt
   ```
2. **Run Data Preprocessing:**

   ```bash
   python scripts/01_data_preprocessing.py
   ```
3. **Run Feature Engineering:**

   ```bash
   python scripts/02_feature_engineering.py
   ```
4. **Perform Exploratory Analysis:**

   ```bash
   python scripts/03_exploratory_analysis.py
   ```
5. **Generate Time-Series Forecasts:**

   ```bash
   python scripts/04_time_series_forecasting.py
   ```
6. **Train and Evaluate Predictive Models:**

   ```bash
   python scripts/05_predictive_modeling.py
   ```
7. **Run Scenario Simulations:**

   ```bash
   python scripts/06_scenario_simulation.py
   ```

All outputs will be saved under the `outputs/` directory.

