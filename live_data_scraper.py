import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from csv import writer
from users_for_saving_data import save_address

def live_data_scraping():
    timestamp = time.time()
    date = datetime.fromtimestamp(timestamp)
    str_date = date.strftime("%Y-%m-%d")

    headers = ['Miestas', 'PM2.5', 'PM10', 'O3', 'Date']
    weather_data = []

    url = "https://aqicn.org/city/lithuania/kaunas-noreikiskes/#/w/lt"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    kaunas_weather_data = []

    miestas = soup.find('div', id='aqiwgttitle', class_='aqiwgt-table-title').text.strip().split(' ')[0]
    pm25 = soup.find('td', id='cur_pm25', class_='tdcur', style='font-weight:bold;font-size:11px;', align='center').text.strip()
    pm10 = soup.find('td', id='cur_pm10', class_='tdcur', style='font-weight:bold;font-size:11px;', align='center').text.strip()
    o3 = soup.find('td', id="cur_o3", class_="tdcur", style='font-weight:bold;font-size:11px;', align="center").text.strip()

    kaunas_weather_data.append((miestas, pm25, pm10, o3, str_date))
    kaunas_weather_quality = pd.DataFrame(kaunas_weather_data, columns=headers)



    url = "https://aqicn.org/city/lithuania/klaipeda-silutes-pl."
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    klaipeda_weather_data = []

    miestas = soup.find('div', id='aqiwgttitle', class_='aqiwgt-table-title').text.strip().split(' ')[0]
    pm25 = soup.find('td', id='cur_pm25', class_='tdcur', style='font-weight:bold;font-size:11px;', align='center').text.strip()
    pm10 = soup.find('td', id='cur_pm10', class_='tdcur', style='font-weight:bold;font-size:11px;', align='center').text.strip()
    o3 = soup.find('td', id="cur_o3", class_="tdcur", style='font-weight:bold;font-size:11px;', align="center").text.strip()
    # so2 = soup.find('td', id='cur_so2', class_='tdcur', style='font-weight:bold;font-size:11px;', align='center').text.strip()

    klaipeda_weather_data.append((miestas, pm25, pm10, o3, str_date))
    klaipeda_weather_quality = pd.DataFrame(klaipeda_weather_data,columns=headers)



    url = "https://aqicn.org/city/lithuania/vilnius-zirmunai"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    vilnius_weather_data = []

    miestas = soup.find('div', id='aqiwgttitle', class_='aqiwgt-table-title').text.strip().split(' ')[0]
    pm25 = soup.find('td', id='cur_pm25', class_='tdcur', style='font-weight:bold;font-size:11px;', align='center').text.strip()
    pm10 = soup.find('td', id='cur_pm10', class_='tdcur', style='font-weight:bold;font-size:11px;', align='center').text.strip()
    o3 = soup.find('td', id="cur_o3", class_="tdcur", style='font-weight:bold;font-size:11px;', align="center").text.strip()
    # so2 = soup.find('td', id='cur_so2', class_='tdcur', style='font-weight:bold;font-size:11px;', align='center').text.strip()

    vilnius_weather_data.append((miestas, pm25, pm10, o3, str_date))
    vilnius_weather_quality = pd.DataFrame(vilnius_weather_data, columns=headers)


    weather_quality = pd.concat([kaunas_weather_quality, klaipeda_weather_quality, vilnius_weather_quality])
    weather_quality.reset_index()
    # print(weather_quality)

    # weather_quality.to_csv(f'{save_address}live_data.csv', index=False)

    df = pd.read_csv(f'{save_address}csv/live_data.csv')

    ### reading existing csv file and its data
    with open(f'{save_address}csv/live_data.csv', 'r') as fp:
        existing_csv = fp.read()

    ### check if todays data is in the csv file if not, new data is appended
    if df['Date'].str.contains(str_date).any():
        print("Siandienos duomenys jau buvo issaugoti")
    else:
        weather_quality.to_csv(f'{save_address}csv/live_data.csv', mode='a', index=False, header=False)
        print('Nauji duomenys sekmingai prideti prie "live_data" failo')

# live_data_scraping()