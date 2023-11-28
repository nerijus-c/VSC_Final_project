import requests
import folium
import time
from users_for_saving_data import save_address

def live_air_quality_monitoring_scraper():
    #API connection and retrieval of a data from a website:
    def vilnius_city():
        vilnius = 'Vilnius'
        api_key = '9720d7c113b9da2456b31dfb4d8f07c05a0cbb65'
        url = f'https://api.waqi.info/feed/{vilnius}/?token={api_key}'
        response = requests.get(url)
        json_data = response.json()
        aqi = json_data['data']['aqi']
        pm25 = json_data['data']['iaqi']['pm25']['v']
        pm10 = json_data['data']['iaqi']['pm10']['v']
        o3 = json_data['data']['iaqi']['o3']['v']
        return f'Vilnius Air Quality Data: AQI={aqi}; PM2.5={pm25}; PM10={pm10}; O3={o3}'

    def kaunas_city():
        kaunas = 'Kaunas'
        api_key = '9720d7c113b9da2456b31dfb4d8f07c05a0cbb65'
        url = f'https://api.waqi.info/feed/{kaunas}/?token={api_key}'
        response = requests.get(url)
        json_data = response.json()
        aqi = json_data['data']['aqi']
        pm25 = json_data['data']['iaqi']['pm25']['v']
        pm10 = json_data['data']['iaqi']['pm10']['v']
        o3 = json_data['data']['iaqi']['o3']['v']
        return f'Kaunas Air Quality Data: AQI={aqi}; PM2.5={pm25}; PM10={pm10}; O3={o3}'

    def klaipeda_city():
        klaipeda = 'Klaipeda'
        api_key = '9720d7c113b9da2456b31dfb4d8f07c05a0cbb65'
        url = f'https://api.waqi.info/feed/{klaipeda}/?token={api_key}'
        response = requests.get(url)
        json_data = response.json()
        aqi = json_data['data']['aqi']
        pm25 = json_data['data']['iaqi']['pm25']['v']
        pm10 = json_data['data']['iaqi']['pm10']['v']
        o3 = json_data['data']['iaqi']['o3']['v']
        return f'Klaipėda Air Quality Data: AQI={aqi}; PM2.5={pm25}; PM10={pm10}; O3={o3}'

    def naujoji_akmene_city():
        url = 'https://api.waqi.info/feed/@3325/?token=9720d7c113b9da2456b31dfb4d8f07c05a0cbb65'
        response = requests.get(url)
        json_data = response.json()
        aqi = json_data['data']['aqi']
        pm25 = json_data['data']['iaqi']['pm25']['v']
        pm10 = json_data['data']['iaqi']['pm10']['v']
        so2 = json_data['data']['iaqi']['so2']['v']
        return f'Naujoji Akmenė Air Quality Data: AQI={aqi}; PM2.5={pm25}; PM10={pm10}; SO2={so2}'

    def rietavas_city():
        url = 'https://api.waqi.info/feed/@3320/?token=9720d7c113b9da2456b31dfb4d8f07c05a0cbb65'
        response = requests.get(url)
        json_data = response.json()
        aqi = json_data['data']['aqi']
        o3 = json_data['data']['iaqi']['o3']['v']
        so2 = json_data['data']['iaqi']['so2']['v']
        return f'Rietavas Air Quality Data: AQI={aqi}; O3={o3}; SO2={so2}'



    # Create a map with live data:

    def live_map_creation():
        live_map = folium.Map(tiles='OpenStreetMap', location=(55.11201074940712, 24.065172740215825), zoom_start=8)

        popup_vilnius = folium.Popup(vilnius_city(), max_width=500)
        popup_kaunas = folium.Popup(kaunas_city(), max_width=500)
        popup_klaipeda = folium.Popup(klaipeda_city(), max_width=500)
        popup_naujoji_akmene = folium.Popup(naujoji_akmene_city(), max_width=500)
        popup_rietavas = folium.Popup(rietavas_city(), max_width=500)

        folium.Marker(
            location=[54.68906449, 25.27499907],
            tooltip='Click here for more info!',
            popup= popup_vilnius,
            icon=folium.Icon(icon='cloud'),
        ).add_to(live_map)

        folium.Marker(
            location=[54.91064874, 23.89693172],
            tooltip='Click me!',
            popup= popup_kaunas,
            icon=folium.Icon(icon='cloud'),
        ).add_to(live_map)

        folium.Marker(
            location=[55.72646869, 21.12991317],
            tooltip='Click me!',
            popup= popup_klaipeda,
            icon=folium.Icon(icon='cloud'),
        ).add_to(live_map)

        folium.Marker(
            location=[56.31768759773947, 22.89277557811417],
            tooltip='Click here!',
            popup=popup_naujoji_akmene,
            icon=folium.Icon(icon='cloud'),
        ).add_to(live_map)


        folium.Marker(
            location=[55.72564804568164, 21.931172247247403],
            tooltip='Click here!',
            popup= popup_rietavas,
            icon=folium.Icon(icon='cloud'),
        ).add_to(live_map)

        live_map.save(f'{save_address}html/live_map.html')
        print("Live map html successfully created and saved")

    live_map_creation()

# def map_update():
#     while True:
#         live_air_quality_monitoring_scraper()
#         time.sleep(10800)