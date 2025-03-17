import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # data cleaning: update null NOAA values with mean of lower and upper
    mean_error_bound = (df['Lower Error Bound'] + df['Upper Error Bound']) / 2
    df['NOAA Adjusted Sea Level'] = df['NOAA Adjusted Sea Level'].fillna(mean_error_bound)

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()