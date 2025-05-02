
# 1. Import pandas, numpy, scikit-learn modules
# 2. Load features.csv and target.csv
# 3. Split into train/test (e.g. 80/20)
# 4. Define models: LinearRegression, RandomForestRegressor
# 5. For each model:
#      a. Train on train set
#      b. Predict on test set
#      c. Compute MSE and R2
#      d. Save metrics to a dict
# 6. Choose best model (e.g. by R2), save model via joblib to '../outputs/best_model.pkl'
# 7. Save metrics summary to '../outputs/metrics.csv'
# 8. If RandomForest chosen, save feature importances to '../outputs/feature_importances.csv'
