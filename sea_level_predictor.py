import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create first line of best fit
    model = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = model.slope
    intercept = model.intercept

    #extend first line of best fit till 2050
    #create an array of years from 1880 to 2050 for x-axis
    years_extended1 = np.arange(1880, 2051, 1)
    line1_y = [intercept + slope*x1 for x1 in years_extended1]


    # Create second line of best fit
    #create new dataframe with values from year 2000 onwards
    df_2000 = df.loc[df['Year'] >= 2000]

    #generate linear regression model for the new dataframe 
    new_model = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    new_slope = new_model.slope
    new_intercept = new_model.intercept

    #extend second line till 2050
    years_extended2 = np.arange(2000, 2051, 1)
    line2_y = [new_intercept + new_slope*x2 for x2 in years_extended2]

    # Bring it all together and add labels and title
    fig, ax = plt.figure(figsize = (10,6)), plt.scatter(x=df['Year'], y= df['CSIRO Adjusted Sea Level'])
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.plot(years_extended1, line1_y, 'g')
    plt.plot(years_extended2, line2_y, 'r')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()