# Fuel Price Watcher Script

import datetime
import requests
from bs4 import BeautifulSoup as soup
import sqlite3

def FuelTr_update(date,comp,fuel,diesel,lpg):
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS FuelTr(Date TEXT,CompanyName TEXT,GasPrice REAL,Diesel REAL,LPG REAL)")
    con.commit()
    data = cursor.execute("SELECT * FROM FuelTr ORDER BY Date DESC LIMIT 1")
    data = cursor.fetchone()[0]
    if data == date:
        print ("Bugün için veri girişi yapılmış.")
    else:
        insert_with_param = """INSERT INTO FuelTr (Date,CompanyName,GasPrice,Diesel,LPG) VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (date,comp,fuel,diesel,lpg)
        cursor.execute(insert_with_param, data_tuple)
        con.commit()
        print ("Yeni veri girişi yapıldı.")
    con.close()

today = str(datetime.date.today())
company = "Aytemiz Petrol"
url = "https://www.aytemiz.com.tr/"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = requests.get(url, headers=header)
page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
fuel_price = page_soup.find_all('div', {"class":"fuel-price"})[0].text.strip().strip('TL/LT')
diesel_price = page_soup.find_all('div', {"class":"fuel-price"})[1].text.strip().strip('TL/LT')
lpg_price = page_soup.find_all('div', {"class":"fuel-price"})[3].text.strip().strip('TL/LT')

req = requests.get(url, headers=header)
page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
fuel_price = page_soup.find_all('div', {"class":"fuel-price"})[0].text.strip().strip('TL/LT')
diesel_price = page_soup.find_all('div', {"class":"fuel-price"})[1].text.strip().strip('TL/LT')
lpg_price = page_soup.find_all('div', {"class":"fuel-price"})[3].text.strip().strip('TL/LT')

def main():
    FuelTr_update(today,company,fuel_price,diesel_price,lpg_price)

if __name__ == "__main__":
    main()
