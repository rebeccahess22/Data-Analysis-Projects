import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.show()


    # Create first line of best fit
    #calculate the line of best fit for the data
    slope, intercept, r_value, p_value, std_err =linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    #extend the x axis to 2050
    years_extended = pd.Series(range(1880, 2051))
    print(years_extended)
    #calculate the y values for the extended x axis
    y_values_extended = slope * years_extended + intercept

    #calculate the line of best fit for the extended data
    #slope_extended, intercept_extended, r_value_extended, p_value_extended, std_err_extended = linregress(y_values_extended, years_extended)

    #plot the line of best fit
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='mediumaquamarine')
    plt.plot(years_extended, slope * years_extended + intercept, color='orchid', label='Best Fit Line')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend(['Data', 'Best Fit Line'])
    plt.show()


    # Create second line of best fit
    #calculate the line of best fit for the data from 2000 onwards
    slope, intercept, r_value, p_value, std_err =linregress(df.loc[df['Year']>=2000,'Year'], df.loc[df['Year']>=2000, 'CSIRO Adjusted Sea Level'])

    #extend the x axis to 2050
    years_extended = pd.Series(range(2000, 2051))
    #calculate the y values for the extended x axis
    y_values_extended = slope * years_extended + intercept

    #plot the line of best fit
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='mediumaquamarine')
    plt.plot(years_extended, slope * years_extended + intercept, color='orchid', label='Best Fit Line')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend(['Data', 'Best Fit Line'])
    plt.show()


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()