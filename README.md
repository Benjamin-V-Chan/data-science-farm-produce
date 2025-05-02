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

