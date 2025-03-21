import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Load data
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', alpha=0.6)
    
    # First line of best fit (using all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_levels = slope * years_extended + intercept
    ax.plot(years_extended, sea_levels, 'r', label='Best fit line (1880-2050)')
    
    # Second line of best fit (using data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    sea_levels_recent = slope_recent * years_recent + intercept_recent
    ax.plot(years_recent, sea_levels_recent, 'g', label='Best fit line (2000-2050)')
    
    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    
    return fig
