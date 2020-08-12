#main program WvdS
import pandas as pd                                         #needed for dataframe
import matplotlib.pyplot as plt                             #needed for plot
import printcovid as pc                                     #WvdS: separating processing and printing functions
import wworld as wv                                         #WvdS: world view

def calc_data (country_df, country_ref_df):
    country_df['P_cp'] = round(country_df['Confirmed'] / country_df['Population'] * 100, 4)  #% corona % of polulation
    country_df['P_dc'] = round(country_df['Deaths'] / country_df['Confirmed'] * 100, 4)      #% corona % deaths
    country_df['P_dp'] = round(country_df['Deaths'] / country_df['Population'] * 100, 4)     #% corona % of polulation
    #increase rate calculation
    country_df['Increase rate'] = country_df['P_cp'].pct_change(periods = 1)
    #print (country_df)
    return country_df

reference_df = pd.read_csv('data/reference.csv')                                 #read reference data
covid_df = pd.read_csv('data/countries-aggregated.csv',parse_dates=['Date'])     #read country aggregated csv

country1 = input("What country are we looking for: ")
while not (covid_df['Country']==country1).any():
    country1 = input("Try again: what country are we looking for: ")

c1_df = (covid_df.loc[covid_df['Country'] == country1])                         #pick data for country1
c1_df = (c1_df.loc[covid_df['Confirmed'] > 0 ])                                 #filter dates with no COVID
c1_ref_df = (reference_df.loc[reference_df['Country_Region'] == country1])
c1_df['Population'] = (c1_ref_df['Population'].values[0])                       #first line in file has total, no need for sum())
pc.print_data(country1, c1_df, c1_ref_df)

country2 = input("Compare with what country: ")
while not (covid_df['Country']==country2).any():
    country2 = input("Try, again: compare with what country: ")

c2_df = (covid_df.loc[covid_df['Country'] == country2])                         #pick data for country2
c2_df = (c2_df.loc[covid_df['Confirmed'] > 0 ])                                 #filter dates with no COVID
c2_ref_df = (reference_df.loc[reference_df['Country_Region'] == country2])
c2_df['Population'] = (c2_ref_df['Population'].values[0])
pc.print_data(country2, c2_df, c2_ref_df)

c1_df = calc_data(c1_df, c1_ref_df)
c2_df = calc_data(c2_df, c2_ref_df)

pc.print_death(c1_df)
pc.print_death(c2_df)

fig, axes = plt.subplots(nrows=2, ncols=2)
c1_df.plot(ax=axes[0,0], title=country1, x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
c1_df.plot(ax=axes[0,1], title=country1, x='Date', y=['Deaths'])

c2_df.plot(ax=axes[1,0],title=country2, x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
c2_df.plot(ax=axes[1,1],title=country2, x='Date', y=['Deaths'])

fig2, axes2 = plt.subplots(nrows=2, ncols=2)
c1_df.plot(ax=axes2[0,0], title=country1, x='Date', y=['P_cp', 'P_dp'])
c2_df.plot(ax=axes2[1,0], title=country2, x='Date', y=['P_cp', 'P_dp'])

c1_df.plot(ax=axes2[0,1], title=country1, x='Date', y=['P_dc'])
c2_df.plot(ax=axes2[1,1], title=country2, x='Date', y=['P_dc'])

wfig, waxes = plt.subplots(nrows=2, ncols=2)
wv.wview_df.plot(ax=waxes[0,0], title="World", x='Date', y=['Confirmed', 'Recovered', 'Deaths'])
wv.wview_df.plot(ax=waxes[0,1], title="World", x='Date', y=['Increase rate'])
c1_df.plot(ax=waxes[1,0], title=country1, x='Date', y=['Increase rate'])
c2_df.plot(ax=waxes[1,1], title=country2, x='Date', y=['Increase rate'])

plt.show()
