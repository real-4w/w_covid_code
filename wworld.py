#=============================================================================================
#helper module
#=============================================================================================
import pandas as pd                                         #needed for dataframe
import pathlib as pl                                        #needed to browse the filesystem
debug = False
#=============================================================================================
path = pl.Path.cwd().parent / 'covid-19' / 'data' / 'worldwide-aggregated.csv'
if debug == True : print("Loading :", path)
wview_df = pd.read_csv(path,parse_dates=['Date'])
if __name__ == "__main__":    # execute only if run as a script
    print('+-' * 30)
    print(wview_df)
