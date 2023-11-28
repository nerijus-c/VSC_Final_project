import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from final_project import save_address

### using selenium library we create a connection to a website
driver_path = "chromedriver.exe"
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://whoairquality.shinyapps.io/AmbientAirQualityDatabase/")
time.sleep(9)

### since website data is not accesable through direct html adress, using selenium webdriver we create a 'virtual buttons'
accept_button = driver.find_element(By.XPATH, '//*[@id="shiny-modal"]/div/div/div[3]/button')
if accept_button:
    accept_button.click()
else:
    print("Button not found")
time.sleep(2)

explore_the_data_button = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')
if explore_the_data_button:
    explore_the_data_button.click()
else:
    print("'Explore' button not found")
time.sleep(4)

### creating a 'virtual button' to filter only our selected country data
choose_country_button = driver.find_element(By.XPATH, '//*[@id="country_selector"]/div/div/div')
if choose_country_button:
    choose_country_button.click()
else:
    print("Button not found")
time.sleep(5)

element = driver.find_element(By.XPATH,'//*[@id="Country-selectized"]')
if element:
    element.send_keys(input("Iveskite norimos valstybes pavadinima ->"))
    element.send_keys(Keys.ENTER)
else:
    print("Button not found")
time.sleep(5)

### create a 'virtual button' to show 100 value rows of table data
entries_button = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_1_length"]/label/select')
if entries_button:
    entries_button.click()
else:
    print("Button not found")
time.sleep(3)

hundred_button = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_1_length"]/label/select/option[4]')
if hundred_button:
    hundred_button.click()
else:
    print("Button not found")
time.sleep(12)

### create empty list where data will be stored
data = []

### scraping data from website
tbody = driver.find_element(By.XPATH, '//*[@id="DataTables_Table_1"]')
data = []
for tr in tbody.find_elements(By.XPATH, '//tr'):
    row = [item.text for item in tr.find_elements(By.XPATH, ".//td")]
    data.append(row)

### list of column names
columns = ['Nr', 'ISO3', 'Country', 'City', 'Year', 'PM2.5', 'PM10', 'NO2', 'Reference', 'Database_version']

### create dataframe
df = pd.DataFrame(data, columns=columns)
# print(df)
df = df.drop(df.index[0:1])
# df = df.dtypes
# print(df)


### create csv file and save the date
df.to_csv(f'{save_address}csv/who_data_100.csv', index=False)
print("csv file successfully saved")

time.sleep(1)
driver.close()

