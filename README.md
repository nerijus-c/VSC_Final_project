# Air particulate matter monitoring and analysis.
Created by: Žygimantas Rėkus and Nerijus Čiuželis, 2023-11-16
![alt_text](https://github.com/nerijus-c/VSC_Final_project/blob/main/jpeg/img.png)

This is the final project for Data analytics course at Vilnius Coding School. The goal is to get all the necessary data from a web, clean it and analyse. Check how air quality is changing according years, region and compare statistics to live data from different cities in Lithuania. For this project we used Python language with some of its libraries, CSV files for saving data and PowerBi for visualisations.

Libraries used in this project: Pandas, Folium, Timestamp, Selenium, Matplotlib, Beautifulsoup.

## who_data_scraper.py:
Steps:
1. Using Selenium library we createad connection to WHO website.
    (https://whoairquality.shinyapps.io/AmbientAirQualityDatabase/)
2. With Selenium WebDriver we filtered the data on the website.
3. Usind Pandas Dataframe we saved the data into a CSV file.


## live_data_scraper.py:
Steps:
1. We scraped the data of major cities of Lithuania using BeautifulSoup.(https://aqicn.org/)
2. With Pandas we create a dataframe and stored the live data into a CSV file.
3. We created if function to check whether the file exists and has today's, if it doesn't have data then the new data will be appended.
4. live_air_quality_monitoring.py Libraries: Requests, Folium.

## live_air_quality_monitoring.py:
Steps:
1. We connected to a website using Folium and API of https://aqicn.org/.
2. Created interactive map with live data and stored it as html file.

## final_project.py:
This is the main file where all calculations and visuals were made.
Steps:

1. Data cleansing:
   * Adjusted the data types. 
   * Interpolated the missing data.
   * Removed unnecessary columns from our data files.

2. Calculations and visualisations:
   1. We calculated Lithuania's yearly average air pollution of PM2.5, PM10, NO2 using the data from WHO database and visualised it.
        ![alt_text](https://github.com/nerijus-c/VSC_Final_project/blob/main/jpeg/air_stat_by_year.png)
   2. Comparison of air pollution in Lithuania's major cities:
           ![alt_text](https://github.com/nerijus-c/VSC_Final_project/blob/main/jpeg/recent_air_quality_data_major_cities.png)
   3. Air polution by particulate matter:
        * PM2.5 ![alt_text](https://github.com/nerijus-c/VSC_Final_project/blob/main/jpeg/city_pm25_avg.png)
        * PM10 ![alt_text](https://github.com/nerijus-c/VSC_Final_project/blob/main/jpeg/city_PM10_avg.png)
        * NO2 ![alt_text](https://github.com/nerijus-c/VSC_Final_project/blob/main/jpeg/city_NO2_avg.png)
   
3. Live AQI monitoring data map:

    To see the live AQI data of Lithuania please click on the map below:      

    [![Lithuania's AQI map.](https://github.com/nerijus-c/VSC_Final_project/blob/main/html/map_pic.png)](https://nbviewer.org/github/nerijus-c/VSC_Final_project/blob/main/html/live_map.html)

## Conclusion:

We've compared the weather quality data based on the data from WHO. By the point 2.i you can see air pollution data by PM2.5, PM110 and NO2 during the period from 2010 and 2019.
We compared the air pollution data of major Lithuania's cities where you can see what are the differences between those cities.
By 3rd point there is a map created where we can check live data of air quality in Lithuania.

