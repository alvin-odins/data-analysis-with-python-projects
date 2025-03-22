
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Task 1: Import the data using Pandas
data = pd.read_csv('epa-sea-level.csv')

# Task 2: Create a scatter plot
plt.figure(figsize=(10,6))
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Data', color='blue')

# Task 3: Calculate the line of best fit for all the data
slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

# Plot the line of best fit for all the data (Year 1880 through to the most recent year)
years_extended = range(1880, 2051)  # Extend the years from 1880 to 2050
sea_level_fit_all_years = [slope * year + intercept for year in years_extended]
plt.plot(years_extended, sea_level_fit_all_years, color='red', label='Fit Line (1880-2050)', linewidth=2)

# Task 4: Calculate the line of best fit just using the data from 2000 onward
data_recent = data[data['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])

# Plot the line of best fit from 2000 onward
sea_level_fit_recent_years = [slope_recent * year + intercept_recent for year in years_extended]
plt.plot(years_extended, sea_level_fit_recent_years, color='green', label='Fit Line (2000-2050)', linewidth=2)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Show the plot
plt.show()