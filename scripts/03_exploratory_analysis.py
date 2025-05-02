import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def load_processed(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=['ref_date'])

def summary_stats(df: pd.DataFrame):
    print(df.describe())

def plot_and_save(df: pd.DataFrame, out_dir: str):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    
    # Histogram of price
    df['average_farm_price'].hist()
    plt.title("Average Farm Price")
    plt.savefig(f"{out_dir}/hist_price.png")
    plt.clf()
    
    # Boxplot of yield by crop
    df.boxplot(column='average_yield', by='crop', rot=45)
    plt.title("Yield by Crop"); plt.suptitle("")
    plt.savefig(f"{out_dir}/box_yield_by_crop.png")
    plt.clf()
    
    # Time series for top 3 provinces by avg production
    top3 = df.groupby('geo')['total_production'].mean().nlargest(3).index
    for prov in top3:
        sub = df[df['geo']==prov]
        plt.plot(sub['ref_date'], sub['total_production'], label=prov)
    plt.legend(); plt.title("Production Trends")
    plt.savefig(f"{out_dir}/ts_top3_provinces.png")
    plt.clf()

def save_corr(df: pd.DataFrame, out_path: str):
    corr = df.select_dtypes(include='number').corr()
    corr.to_csv(out_path)

if __name__ == "__main__":
    df = load_processed("../outputs/processed_data.csv")
    summary_stats(df)
    save_corr(df, "../outputs/correlation_matrix.csv")
    plot_and_save(df, "../outputs/figures")
