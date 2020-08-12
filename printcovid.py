
def print_data(country, country_df, country_ref_df):
    print('+-' * 30)
    print(f"Earliest infection in {country}: ", country_df['Date'].min())
    print(f"Latest data for {country}: ", country_df['Date'].max())
    print(f"Total population for {country}", country_ref_df['Population'].sum())
    print(f"Detailed reference data for {country}:")
    print(country_ref_df)
    #print(country_df)

def print_death(country_df):
    print('+-' * 30)
    print(country_df[['Country', 'Deaths', 'P_cp', 'P_dc', 'P_dp']])
