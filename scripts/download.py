from urllib.request import urlretrieve
import os

output_relative_dir = '../data/raw/'

# check if it exists
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# create the paths for the data
for target_dir in ('tlc_data', 'other_data'): # taxi_zones, weather should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)

                    
YEARS = ['2018', '2019']
MONTHS = range(1, 13)

# Taxi URL template as of 08/2022
yellow_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"#year-monnth

# data output directory is `data/tlc_data/`
yellow_output_dir = output_relative_dir + 'tlc_data'
weather_output_dir = output_relative_dir + 'other_data/weather'
                    
# download yellow taxi trip data
for year in YEARS:
    for month in MONTHS:
        # 0-fill i.e 1 -> 01, 2 -> 02, etc
        month = str(month).zfill(2) 
        print(f"Begin downloading yellow taxi trip data year {year} - month {month}")

        # generate url
        url = f'{yellow_url}{year}-{month}.parquet'
        # generate output location and filename
        output_dir = f"{yellow_output_dir}/{year}-{month}.parquet"
        # download
        urlretrieve(url, output_dir) 

        print(f"Completed year {year} - month {month}")
    
    