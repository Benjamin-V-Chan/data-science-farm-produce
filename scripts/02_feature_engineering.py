import pandas as pd
from pathlib import Path

def load_processed(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=['ref_date'])

def engineer_features(df: pd.DataFrame) -> (pd.DataFrame, pd.Series):
    df = df.sort_values(['geo', 'crop', 'ref_date'])
    # Year-over-year pct changes
    df['pct_change_price']      = df.groupby(['geo','crop'])['average_farm_price'].pct_change().fillna(0)
    df['pct_change_yield']      = df.groupby(['geo','crop'])['average_yield'].pct_change().fillna(0)
    df['pct_change_production'] = df.groupby(['geo','crop'])['total_production'].pct_change().fillna(0)
    # One-hot encode categorical
    df = pd.get_dummies(df, columns=['geo','crop'], drop_first=True)
    # Features / target
    X = df.drop(columns=['total_farm_value','ref_date'])
    y = df['total_farm_value']
    return X, y

def save_data(X: pd.DataFrame, y: pd.Series, out_x: str, out_y: str):
    Path(out_x).parent.mkdir(parents=True, exist_ok=True)
    X.to_csv(out_x, index=False)
    y.to_frame('total_farm_value').to_csv(out_y, index=False)

if __name__ == "__main__":
    df = load_processed("../outputs/processed_data.csv")
    X, y = engineer_features(df)
    save_data(X, y, "../outputs/features.csv", "../outputs/target.csv")
