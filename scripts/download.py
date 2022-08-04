from urllib.request import urlretrieve
import os

# from the current `tute_1` directory, go back two levels to the `MAST30034` directory
output_relative_dir = '../data/raw/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# now, for each type of data set we will need, we will create the paths
for target_dir in ('tlc_data', 'other_data'): # taxi_zones should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)
        
YEARS = ['2021', '2022']
# adjust the range function to the numerical months i.e 1 = jan, 2 = feb, etc...
# MONTHS = range(1, 13)
MONTHS = range(1, 13)
# this is the URL template as of 07/2022
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"#year-month.parquet

# data output directory is `data/tlc_data/`
tlc_output_dir = output_relative_dir + 'tlc_data'

for year in YEARS:
    if year == "2022":
        MONTHS = range(1, 5)
    for month in MONTHS:
        # 0-fill i.e 1 -> 01, 2 -> 02, etc
        month = str(month).zfill(2) 
        print(f"Begin downloading Yellow Taxi Trip data year {year} - month {month}")

        # generate url
        url = f'{URL_TEMPLATE}{year}-{month}.parquet'
        # generate output location and filename
        output_dir = f"{tlc_output_dir}/{year}-{month}.parquet"
        # download
        urlretrieve(url, output_dir) 

        print(f"Completed year {year} - month {month}")