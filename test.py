# Import system and name from os for clear function
from os import system, name
# import sqlite3
# from beautifultable import BeautifulTable
from bs4 import BeautifulSoup as soup
from datetime import datetime
import urllib.request

# def menu_car_brands():
#     con = sqlite3.connect("car.db")
#     cursor = con.cursor()
#     cursor.execute("SELECT BrandID, Brand FROM CarBrands ORDER BY Brand")
#     data = cursor.fetchall()
#     table = BeautifulTable()
#     table.set_style(BeautifulTable.STYLE_COMPACT)
#     table.columns.header = ["Marka ID", "Marka"]
#     table.columns.alignment = BeautifulTable.ALIGN_LEFT
#     for i in data:
#         table.rows.append([i[0],i[1]])
#     print(table)
#     con.close()
# # menu_car_brands()

# def menu_car_models(inp):
#     con = sqlite3.connect("car.db")
#     cursor = con.cursor()
#     cursor.execute("SELECT CarID, CarBrand, CarModel FROM ElectricCar WHERE CarBrand=? ORDER BY CarModel", (inp,))
#     data = cursor.fetchall()
#     table = BeautifulTable()
#     table.set_style(BeautifulTable.STYLE_COMPACT)
#     table.columns.header = ["ID", "Marka", "Model"]
#     table.columns.alignment = BeautifulTable.ALIGN_LEFT
#     con.close()
#     for i in data:
#         table.rows.append([i[0],i[1],i[2]])
#     return(table)

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Table Width
tbl_len_out = 72
tbl_len_in = 18

def url_hunter(url):
    # now = datetime.now()
    # today = now.strftime("%d/%m/%Y")
    # time = now.strftime("%H:%M:%S")

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    uClient = urllib.request.urlopen(req)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
    brand_name = page_soup.find('title').text.strip().split(" price",1)[0].split(" ",1)[0]
    model_name = page_soup.find('title').text.strip().split(" price",1)[0].split(" ",1)[1]
    total_power = page_soup.find_all('div', {"class":"data-table"})[2].find_all("td")[7].text.strip().split(" kW",1)[0]
    total_torque = page_soup.find_all('div', {"class":"data-table"})[2].find_all("td")[9].text.strip().split(" Nm",1)[0]
    battery_capacity = page_soup.find_all('div', {"class":"data-table"})[3].find_all("td")[1].text.strip().split(" kWh",1)[0]
    battery_useable = page_soup.find_all('div', {"class":"data-table"})[3].find_all("td")[3].text.strip().split(" kWh",1)[0]
    range_wltp = page_soup.find_all('div', {"class":"data-table has-legend"})[2].find_all('div', {"class":"inline-block"})[2].find_all("td")[1].text.strip().split(" km",1)[0]
    range_city_cold_weather = page_soup.find_all('div', {"class":"data-table has-legend"})[1].find_all("td")[1].text.strip().split(" km",1)[0]
    range_highway_cold_weather = page_soup.find_all('div', {"class":"data-table has-legend"})[1].find_all("td")[3].text.strip().split(" km",1)[0]
    range_combined_cold_weather = page_soup.find_all('div', {"class":"data-table has-legend"})[1].find_all("td")[5].text.strip().split(" km",1)[0]
    range_city_mild_weather = page_soup.find_all('div', {"class":"data-table has-legend"})[1].find_all("td")[7].text.strip().split(" km",1)[0]
    range_highway_mild_weather = page_soup.find_all('div', {"class":"data-table has-legend"})[1].find_all("td")[9].text.strip().split(" km",1)[0]
    range_combined_mild_weather = page_soup.find_all('div', {"class":"data-table has-legend"})[1].find_all("td")[11].text.strip().split(" km",1)[0]

    return(brand_name, model_name, total_power, total_torque, battery_capacity, battery_useable, range_wltp, range_city_cold_weather, range_highway_cold_weather, range_combined_cold_weather, range_city_mild_weather, range_highway_mild_weather, range_combined_mild_weather)
    # return(range_wltp)

# Table dimentions
tbl_len_out = 90
tbl_len_in = 38
tbl_len_car = 25

# url = "https://ev-database.org/car/1591/Tesla-Model-3-Long-Range-Dual-Motor"
# url = "https://ev-database.org/car/1319/Dacia-Spring-Electric"
# car_data = url_hunter(url)

# clear()
print(f"\n{' URL Data Hunter':=^{tbl_len_out}}")
inp_url = input(f"\n{' URL Kaynağı':<{25}} : ")
# print(f"{' Tarih':<{tbl_len_in}} : {today}")
# print(f"{' Zaman':<{tbl_len_in}} : {time}")
# print(url_hunter(url))

car_data = url_hunter(inp_url)
print(f"\n{'':-^{tbl_len_out}}")
print(f"\n {'Marka':{tbl_len_car}}: {car_data[0]}")
print(f" {'Model':{tbl_len_car}}: {car_data[1]}")
print(f" {'Model yılı':{tbl_len_car}}: 2022")
print(f" {'Motor Gücü':{tbl_len_car}}: {car_data[2]} kW")
print(f" {'Tork':{tbl_len_car}}: {car_data[3]} Nm")

print(f"\n {'Batarya Kapasitesi':{tbl_len_car}}: {car_data[4]} kWh")
print(f" {'Kullanılabilir Kapasite':{tbl_len_car}}: {car_data[5]} kWh")

print(f"\n {'WLTP Menzili':{tbl_len_car}}: {car_data[6]} km")

print(f"\n {'-10°C Hava Sıcaklığında':{tbl_len_car}}  Menzil (Klima açık)")
print(f" {'':-^{tbl_len_car}}  {'':-^{10}}")
print(f" {'Şehiriçi Menzili':{tbl_len_car}}: {car_data[7]} km")
print(f" {'Şehirdışı Menzili':{tbl_len_car}}: {car_data[8]} km")
print(f" {'Karma Menzili':{tbl_len_car}}: {car_data[9]} km")

print(f"\n {'23°C Hava Sıcaklığında':{tbl_len_car}}  Menzil (Klima kapalı)")
print(f" {'':-^{tbl_len_car}}  {'':-^{10}}")
print(f" {'Şehiriçi Menzili':{tbl_len_car}}: {car_data[10]} km")
print(f" {'Şehirdışı Menzili':{tbl_len_car}}: {car_data[11]} km")
print(f" {'Karma Menzili':{tbl_len_car}}: {car_data[12]} km")

print(f"\n{'':=^{tbl_len_out}}\n")