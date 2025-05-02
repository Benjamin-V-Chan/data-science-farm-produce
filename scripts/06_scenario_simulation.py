import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

def load_processed(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=['ref_date'])

def simulate_group(df: pd.DataFrame, n_sim: int=1000):
    mu_y, sd_y = df['average_yield'].mean(), df['average_yield'].std()
    mu_p, sd_p = df['average_farm_price'].mean(), df['average_farm_price'].std()
    area = df['seeded_area_hectares'].iloc[-1]
    sims = []
    for i in range(n_sim):
        y_samp = np.random.normal(mu_y, sd_y)
        p_samp = np.random.normal(mu_p, sd_p)
        prod   = y_samp * area
        value  = prod * p_samp
        sims.append({'sim': i, 'sim_yield': y_samp, 'sim_price': p_samp,
                     'sim_production': prod, 'sim_value': value})
    return pd.DataFrame(sims)

def run_simulations(df: pd.DataFrame, out_dir: str):
    for (prov, crop), group in df.groupby(['geo','crop']):
        sims = simulate_group(group)
        dir_proc = Path(out_dir)/prov
        dir_proc.mkdir(parents=True, exist_ok=True)
        sims.to_csv(dir_proc/f"{crop}_simulation.csv", index=False)
        plt.hist(sims['sim_value'], bins=50)
        plt.title(f"Value Distribution: {prov} - {crop}")
        plt.savefig(dir_proc/f"{crop}_value_dist.png")
        plt.clf()

if __name__ == "__main__":
    df = load_processed("../outputs/processed_data.csv")
    run_simulations(df, "../outputs/simulations")
