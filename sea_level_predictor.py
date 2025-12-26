# sea_level_predictor.py

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    ax.plot(x1, intercept1 + slope1 * pd.Series(x1))

    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    x2 = range(2000, 2051)
    ax.plot(x2, intercept2 + slope2 * pd.Series(x2), color="red")

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig('sea_level_plot.png')
    return fig
