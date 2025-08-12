import pandas as pd
import matplotlib.pyplot as plt # type: ignore
from scipy.stats import linregress # type: ignore
def draw_plot():
    df=pd.read_csv("epa-sea-level.csv")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    ax.plot(years_extended, intercept + slope * years_extended, 'r', label='Best fit: All data')

    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent_extended = pd.Series(range(2000, 2051))
    ax.plot(years_recent_extended, intercept_recent + slope_recent * years_recent_extended, 'g', label='Best fit: 2000+ data')

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()




