from urllib.request import urlretrieve
import os

output_relative_dir = '../data/raw/'

# check if it exists
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# create the paths for the data
for target_dir in ('tlc_data', 'other_data'): # taxi_zones should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)
        
YEARS = ['2021', '2022']
MONTHS = range(4, 13)

# this is the URL template as of 07/2022
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"

# data output directory is `data/tlc_data/`
tlc_output_dir = output_relative_dir + 'tlc_data'

# download yellow taxi trip data
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


    