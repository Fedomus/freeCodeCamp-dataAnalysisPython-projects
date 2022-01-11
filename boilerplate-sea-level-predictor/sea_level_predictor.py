import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    # Read data from file
    df = pd.read_csv('FreeCodeCamp\Data analysis\\boilerplate-sea-level-predictor\epa-sea-level.csv')

    # Create scatter plot
    years = df['Year']
    seaLevel = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.scatter(years, seaLevel, s=50, alpha=0.5)


    # Create first line of best fit
    lineReg1 = linregress(years, seaLevel)
    slope = lineReg1.slope
    intercept = lineReg1.intercept
    lineFunc = lambda x: slope * x + intercept
    years1 = [y for y in range(1880, 2051)]
    line1 = list(map(lineFunc, years1))
    plt.plot(years1,line1, 'b')

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    yearsRecent = df2['Year']
    seaLevelRecent = df2['CSIRO Adjusted Sea Level']
    lineReg2 = linregress(yearsRecent, seaLevelRecent)
    slope = lineReg2.slope
    intercept = lineReg2.intercept
    years2 = [y for y in range(2000, 2051)]
    line2 = list(map(lineFunc, years2))
    plt.plot(years2, line2, 'r')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()