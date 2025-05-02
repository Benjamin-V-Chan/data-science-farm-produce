
# 1. Import pandas
# 2. Load processed_data.csv
# 3. Sort by province, crop, year
# 4. For each group, compute year-over-year pct change for:
#      - average_price
#      - average_yield
#      - total_production
# 5. Fill any NaNs from first diff with zero
# 6. One-hot encode 'province' and 'crop' columns
# 7. Define feature matrix X and target vector y (e.g. target = total_farm_value)
# 8. Save X to '../outputs/features.csv' and y to '../outputs/target.csv'
