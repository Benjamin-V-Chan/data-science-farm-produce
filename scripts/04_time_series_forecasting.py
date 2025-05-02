
# 1. Import pandas, numpy, statsmodels.tsa.holtwinters
# 2. Load processed_data.csv
# 3. For each (province, crop) group:
#      a. Set 'year' as index
#      b. Fit an ExponentialSmoothing model on total_production
#         with trend='add', seasonal=None
#      c. Forecast next 5 years
#      d. Append forecasts to a list
#      e. Plot history + forecast, save figure
# 4. Concatenate all forecasts and save to '../outputs/forecasts.csv'
