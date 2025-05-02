import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt
from pathlib import Path

def load_processed(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=['ref_date'])

def forecast_group(df: pd.DataFrame, periods: int=5):
    df = df.set_index('ref_date').asfreq('Y')
    model = ExponentialSmoothing(df['total_production'], trend='add', seasonal=None)
    fit = model.fit(optimized=True)
    fcast = fit.forecast(periods)
    return fcast

def run_forecasts(df: pd.DataFrame, out_csv: str, figs_dir: str):
    Path(figs_dir).mkdir(parents=True, exist_ok=True)
    records = []
    for (prov, crop), group in df.groupby(['geo','crop']):
        ts = group[['ref_date','total_production']].rename(columns={'ref_date':'ds','total_production':'y'}).set_index('ds')
        fcast = forecast_group(group)
        for year, val in fcast.items():
            records.append({'geo':prov, 'crop':crop, 'year':year.year, 'forecast_production':val})
            
        # plot
        plt.plot(ts.index, ts['y'], label='history')
        plt.plot(fcast.index, fcast.values, label='forecast')
        plt.title(f"{prov} - {crop}")
        plt.legend()
        plt.savefig(f"{figs_dir}/{prov}_{crop}_forecast.png")
        plt.clf()
    pd.DataFrame.from_records(records).to_csv(out_csv, index=False)

if __name__ == "__main__":
    df = load_processed("../outputs/processed_data.csv")
    run_forecasts(df, "../outputs/forecasts.csv", "../outputs/figures/forecasts")
