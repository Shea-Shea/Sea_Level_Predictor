import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df_sea = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot and add labels and title
    fig = plt.figure(figsize=(16, 6))
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=df_sea, color='red')
    # plt.show()

    # Create first line of best fit
    # Create list of years from 1880 to 2050 and turn it into a data frame to be used in plotting best fit line
    extend_year_list = [year for year in range(1880, 2051, 1)]
    df_ext_yr = pd.DataFrame(extend_year_list, columns=['Year'])
    del extend_year_list
    reg = linregress(
        df_sea['Year'], df_sea['CSIRO Adjusted Sea Level'])

    plt.plot(df_ext_yr['Year'], reg.slope*df_ext_yr['Year']+reg.intercept)
    # Create second line of best fit
    reg_start = df_sea[df_sea['Year'] == 2000].index[0]
    reg2_start = df_ext_yr[df_ext_yr['Year'] == 2000].index[0]
    reg_2 = linregress(
        df_sea['Year'].iloc[reg_start:], df_sea['CSIRO Adjusted Sea Level'].iloc[reg_start:])

    plt.plot(df_ext_yr['Year'].iloc[reg2_start:], reg_2.slope *
             df_ext_yr['Year'].iloc[reg2_start:]+reg_2.intercept)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()