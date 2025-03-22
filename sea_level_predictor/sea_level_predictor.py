
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    mean_err_bound = (df['Lower Error Bound'] + df['Upper Error Bound']) / 2
    df['NOAA Adjusted Sea Level'] = df['NOAA Adjusted Sea Level'].fillna(mean_err_bound)

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = range(df['Year'].min(), 2051)
    sea_levels_extended = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_levels_extended, label='Best Fit Line (All Data)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_recent_extended = range(2000, 2051)
    sea_levels_recent_extended = [slope_recent * year + intercept_recent for year in years_recent_extended]
    plt.plot(years_recent_extended, sea_levels_recent_extended, label='Best Fit Line (2000 onwards)', color='orange')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(loc='best')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('example/sea_level_plot.png')
    return plt.gca()