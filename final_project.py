### import libraries
import datetime
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from live_air_quality_monitoring import live_air_quality_monitoring_scraper
from live_data_scraper import live_data_scraping
from users_for_saving_data import save_address
import schedule


### creating log file
logging.basicConfig(filename=f'{save_address}log/scraper.log', level=logging.DEBUG, format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# Read WHO data:
df = pd.read_csv(f'{save_address}csv/who_data_100.csv')
# print(df)

### instead of Null values we interpolate some missing data
df['PM2.5'].interpolate(method='linear', inplace=True, limit_direction='backward')
df['PM10'].interpolate(method='linear', inplace=True)
df['NO2'].interpolate(method='linear', inplace=True)

### removing unnecesary columns and replacing some of the values
df = df.drop(columns=['ISO3', 'Reference', 'Database_version'])
df = df.replace('Šiauliai', 'Siauliai')
df = df.replace('Klaipėda', 'Klaipeda')
df = df.replace('Kėdainiai', 'Kedainiai')
df = df.replace('Mažeikiai', 'Mazeikiai')
df = df.replace('Naujoji Akmenė', 'Naujoji Akmene')
df = df.replace('Panevėžys', 'Panevezys')
df = df.replace('Naujoji Akmene', 'N. Akmene')

### assigning prefered data types to column values
df['PM2.5'] = df['PM2.5'].astype(int)
df['PM10'] = df['PM10'].astype(int)
df['NO2'] = df['NO2'].astype(int)
df['Country'] = df['Country'].astype(str)
df['City'] = df['City'].astype(str)
df['Year'] = df['Year'].astype('int32')
df['Year'] = pd.to_datetime(df.Year, format='%Y')
df['Year'] = df['Year'].dt.strftime('%Y')
# print(df.dtypes)

avg_all = df[['NO2', 'PM10', 'PM2.5']].mean().round(2)
# print(f"Bendras visu matavimu vidurkis (μg/m3) : \n{avg_all} ")

avg_year = df.groupby('Year', as_index=False)[['PM2.5', 'PM10', 'NO2']].mean().round(2)
# print(f"Vidutines reiksmes pagal metus:\n{avg_year}")

avg_city = df.groupby('City', as_index=False)[['PM2.5', 'PM10', 'NO2']].mean().round(2)
# print(f"Vidutines reiksmes pagal miesta:\n{avg_city}")

avg_city_PM25 = df.groupby('City', as_index=False)[['PM2.5']].mean().round(2)
# print(avg_city_PM25)

avg_city_PM10 = df.groupby('City', as_index=False)[['PM10']].mean().round(2)
# print(avg_city_PM25)

avg_city_NO2 = df.groupby('City', as_index=False)[['NO2']].mean().round(2)
# print(avg_city_PM25)

### finding highest  and lowest value points
highest_value_pm25 = np.argmax(avg_year['PM2.5'])
lowest_value_pm25 = np.argmin(avg_year['PM2.5'])

highest_value_pm10 = np.argmax(avg_year['PM10'])
lowest_value_pm10 = np.argmin(avg_year['PM10'])

highest_value_no2 = np.argmax(avg_year['NO2'])
lowest_value_no2 = np.argmin(avg_year['NO2'])

### Calculating min and max values
min_value_pm25 = np.min(avg_year['PM2.5'])
max_value_pm25 = np.max(avg_year['PM2.5'])

min_value_pm10 = np.min(avg_year['PM10'])
max_value_pm10 = np.max(avg_year['PM10'])

min_value_no2 = np.min(avg_year['NO2'])
max_value_no2 = np.max(avg_year['NO2'])

# print(max_value_pm25)

def show_air_quality_statistics_by_year():
    # Adding x variable for X-Axis "Year" values
    x = avg_year['Year']
    plt.figure(figsize=(14, 12))
    plt.plot(x, avg_year['PM2.5'], label='PM2.5', color='green')
    plt.plot(x, avg_year['PM10'], label='PM10', color='blue')
    plt.plot(x, avg_year['NO2'], label='NO2', color='red')

    ### Showing highest and lowest values on visualisation
    plt.plot(highest_value_pm25, max_value_pm25, marker=7, markersize=14, color='magenta', label='Highest value')
    plt.plot(lowest_value_pm25, min_value_pm25, marker=6, markersize=14, color='cyan', label='Lowest value')

    plt.plot(highest_value_pm10, max_value_pm10, marker=7, markersize=14, color='magenta')
    plt.plot(lowest_value_pm10, min_value_pm10, marker=6, markersize=14, color='cyan')

    plt.plot(highest_value_no2, max_value_no2, marker=7, markersize=14, color='magenta')
    plt.plot(lowest_value_no2, min_value_no2, marker=6, markersize=14, color='cyan')

    # add legend
    plt.legend(title='Air quality measures')

    # adding x and y axes with labels and a title
    plt.ylabel('Value μg/m3', fontsize=18)
    plt.xlabel('Year', fontsize=18)
    plt.title('Air quality by year', fontsize=22)
    plt.xticks(x, rotation=90)
    plt.grid()
    plt.savefig(f'{save_address}jpeg/air_stat_by_year')
    plt.show()
# show_air_quality_statistics_by_year()


# def show_city_PM25_average():
#     x = avg_city_PM25['City']
#     plt.figure(figsize=(12, 12))
#     plt.bar(x, avg_city_PM25['PM2.5'], color='green')
#     plt.ylabel('Value μg/m3', fontsize=18)
#     plt.title('Yearly average PM2.5 by city', fontsize=18)
#     plt.xticks(x, rotation=60)
#     plt.rcParams.update({'font.size': 22})
#     plt.savefig(f'{save_address}jpeg/city_pm25_avg')
#     plt.show()
# # show_city_PM25_average()
#
# def show_city_PM10_average():
#     x = avg_city_PM10['City']
#     plt.figure(figsize=(12, 12))
#     plt.bar(x, avg_city_PM10['PM10'], color='blue')
#     plt.ylabel('Value μg/m3', fontsize=18)
#     plt.title('Yearly average PM10 by city', fontsize=18)
#     plt.xticks(x, rotation=60)
#     plt.rcParams.update({'font.size': 22})
#     plt.savefig(f'{save_address}jpeg/city_PM10_avg')
#     plt.show()
# # show_city_PM10_average()
#
# def show_city_NO2_average():
#     x = avg_city_NO2['City']
#     plt.figure(figsize=(12, 12))
#     plt.bar(x, avg_city_NO2['NO2'], color='red')
#     plt.ylabel('Value μg/m3', fontsize=18)
#     plt.title('Yearly average NO2 by city', fontsize=18)
#     plt.xticks(x, rotation=50)
#     plt.rcParams.update({'font.size': 22})
#     plt.savefig(f'{save_address}jpeg/city_NO2_avg')
#     plt.show()
# # show_city_NO2_average()

### show average air quality by city
def show_avg_city():
    cities = avg_city['City']
    particular = avg_city[['PM2.5', 'PM10', 'NO2']]

    x = np.arange(len(cities))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in particular.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Value μg/m3')
    ax.set_title('Air polution particals by city')
    ax.set_xticks(x + width, cities, rotation=90)
    ax.legend(ncols=3)
    ax.set_ylim(0, 35)
    plt.grid(axis='y')
    plt.savefig(f'{save_address}jpeg/city_avg')
    plt.show()

# show_avg_city()

# Update AQI data on daily basis:
live_data_scraping()

# live_data_scraping()
live_df = pd.read_csv(f'{save_address}csv/live_data.csv')
# print(live_df)
filter_vilnius = live_df.loc[live_df['Miestas'] == 'Vilnius']
filter_kaunas = live_df.loc[live_df['Miestas'] == 'Kaunas']
filter_klaipeda = live_df.loc[live_df['Miestas'] == 'Klaipėda']
# print(filter_klaipeda)

def show_air_quality_by_city():
    # Adding x variable for X-Axis "Date" values
    plt.figure(figsize=(14, 12))
    x = filter_kaunas['Date']
    plt.plot(x, filter_kaunas['PM2.5'], label='PM2.5 Kaunas', color='green')
    plt.plot(x, filter_kaunas['PM10'], label='PM10 Kaunas', color='blue')
    plt.plot(x, filter_kaunas['O3'], label='O3 Kaunas', color='red')

    x = filter_vilnius['Date']
    plt.plot(x, filter_vilnius['PM2.5'], label='PM2.5 Vilnius', linestyle=(0, (5, 10)), color='green')
    plt.plot(x, filter_vilnius['PM10'], label='PM10 Vilnius', linestyle=(0, (5, 10)), color='blue')
    plt.plot(x, filter_vilnius['O3'], label='O3 Vilnius', linestyle=(0, (5, 10)), color='red')

    x = filter_klaipeda['Date']
    plt.plot(x, filter_klaipeda['PM2.5'], label='PM2.5 Klaipėda', linestyle=(0, (1, 1)), color='green')
    plt.plot(x, filter_klaipeda['PM10'], label='PM10 Klaipėda', linestyle=(0, (1, 1)), color='blue')
    plt.plot(x, filter_klaipeda['O3'], label='O3 Klaipėda', linestyle=(0, (1, 1)), color='red')

    # add legend
    plt.legend(title='Air quality measures')

    # adding x and y axes with labels and a title
    plt.ylabel('Value μg/m3', fontsize=18)
    plt.xlabel('Date', fontsize=18)
    plt.title('Air quality measures in major cities', fontsize=20)
    plt.xticks(x, rotation=0)
    plt.grid()
    plt.savefig(f'{save_address}jpeg/recent_air_quality_data_major_cities')
    plt.show()

show_air_quality_by_city()


#Updating map:
schedule.every(10800).seconds.do(live_air_quality_monitoring_scraper)

while True:
    schedule.run_pending()
    time.sleep(5)


