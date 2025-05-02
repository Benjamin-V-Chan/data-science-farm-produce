import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def load_features(path_x: str, path_y: str):
    X = pd.read_csv(path_x)
    y = pd.read_csv(path_y)['total_farm_value']
    return X, y

def train_and_eval(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = {
        'LinearRegression': LinearRegression(),
        'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42)
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        r2  = r2_score(y_test, preds)
        results[name] = {'mse': mse, 'r2': r2, 'model': model}
    return results

def save_results(results: dict, out_dir: str):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    rows = []
    for name, res in results.items():
        rows.append({'model': name, 'mse': res['mse'], 'r2': res['r2']})
    pd.DataFrame(rows).to_csv(f"{out_dir}/metrics.csv", index=False)
    best = max(results.items(), key=lambda kv: kv[1]['r2'])
    best_name, best_model = best[0], best[1]['model']
    joblib.dump(best_model, f"{out_dir}/{best_name}_model.pkl")
    
    if best_name == 'RandomForest':
        import numpy as np
        feat_imp = pd.DataFrame({
            'feature': X.columns,
            'importance': best_model.feature_importances_
        }).sort_values('importance', ascending=False)
        feat_imp.to_csv(f"{out_dir}/feature_importances.csv", index=False)

if __name__ == "__main__":
    X, y = load_features("../outputs/features.csv", "../outputs/target.csv")
    results = train_and_eval(X, y)
    save_results(results, "../outputs")
