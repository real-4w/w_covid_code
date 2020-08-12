#==============================================================================
#helper module
#==============================================================================
import pandas as pd                                         #needed for dataframe

wview_df = pd.read_csv('data/worldwide-aggregated.csv',parse_dates=['Date'])

if __name__ == "__main__":    # execute only if run as a script
    print('+-' * 30)
    print(wview_df)
