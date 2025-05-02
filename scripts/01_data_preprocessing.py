import pandas as pd
import numpy as np
from pathlib import Path

def load_raw(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns=lambda x: x.strip().lower().replace(' ', '_'))
    df['ref_date'] = pd.to_datetime(df['ref_date'], format='%Y')
    # Impute numeric missing with median
    nums = df.select_dtypes(include='number').columns
    for col in nums:
        df[col] = df[col].fillna(df[col].median())
    # Derived features
    df['production_per_ha'] = df['total_production'] / df['seeded_area_hectares']
    df['value_per_tonne']   = df['total_farm_value'] / df['total_production']
    return df

def save_clean(df: pd.DataFrame, out_path: str):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    raw = load_raw("../data/farm_production_dataset.csv")
    clean = clean_df(raw)
    save_clean(clean, "../outputs/processed_data.csv")
