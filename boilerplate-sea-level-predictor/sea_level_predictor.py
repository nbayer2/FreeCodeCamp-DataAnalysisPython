import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')    

    # Create scatter plot
    plt.scatter(x=df['Year'], y = df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
    
    X=np.arange(df.Year.min(),2051,1)
    Y= res.intercept + res.slope*X
    plt.plot(X,Y)

    # Create second line of best fit
    df2=df[df.Year>=2000]
    res2 = linregress(df2.Year, df2["CSIRO Adjusted Sea Level"])
    X2=np.arange(2000,2051,1)
    Y2=res2.intercept + res2.slope*X2
    plt.plot(X2,Y2)
    
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
   
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()