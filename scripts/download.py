from urllib.request import urlretrieve
import os

output_relative_dir = '../data/raw/'

# check if it exists
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# create the paths for the data
for target_dir in ('tlc_data', 'test_data', 'weather_data'): 
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)

                    
YEARS = ['2018', '2019']
MONTHS = range(1, 13)

# Taxi URL template as of 08/2022
yellow_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"#year-monnth

# data output directory is `data/tlc_data/`
yellow_output_dir = output_relative_dir + 'tlc_data'
                    
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
        
# download weather data
weather_url = "https://www.ncei.noaa.gov/data/global-hourly/access/" #/year/74486094789.csv
for year in YEARS:
    print(f"Begin downloading {year} weather data")
    output_dir = f"{output_relative_dir}/weather_data/{year}-weather.csv"
    url = f'{weather_url}{year}/74486094789.csv'
    urlretrieve(url, output_dir) 
    print(f"Completed year {year} weather data")

# Test data download
# download taxi test data
print(f"Begin downloading yellow taxi trip data year 2020 - month 01")

year = "2020"
month = "01"
print(f"Begin downloading test data, yellow taxi trip year {year} - month {month}")
url = f'{yellow_url}{year}-{month}.parquet'
output_dir = f"{output_relative_dir}/test_data/test_data.parquet"
# download
urlretrieve(url, output_dir) 

# download weather test data
print(f"Completed year {year} - month {month}")
print(f"Begin downloading weather test data")
url = 'https://www.ncei.noaa.gov/data/global-hourly/access/2020/74486094789.csv'
output_dir = f"{output_relative_dir}/test_data/weather_test_data.csv"
urlretrieve(url, output_dir)
print(f"Completed")