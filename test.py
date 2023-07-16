# TURKIYE FUEL PRICE WATCHER

import datetime
import requests
from bs4 import BeautifulSoup as soup
import sqlite3

def FuelTr_update(date,comp,dist,fuel,diesel,lpg):
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS FuelTr(Date TEXT,CompanyName TEXT, District TEXT, GasPrice REAL,Diesel REAL,LPG REAL)")
    con.commit()
    data = cursor.execute("SELECT * FROM FuelTr ORDER BY Date DESC LIMIT 1")
    data = cursor.fetchone()[0]

    if data == date:
        print ("Bugün için veri girişi yapılmış.")
    else:
        insert_with_param = """INSERT INTO FuelTr (Date,CompanyName,District,GasPrice,Diesel,LPG) VALUES (?, ?, ?, ?, ?, ?);"""
        data_tuple = (date,comp,dist,fuel,diesel,lpg)
        cursor.execute(insert_with_param, data_tuple)
        con.commit()
        print ("Yeni veri girişi yapıldı.")
    con.close()

today = str(datetime.date.today())
company = "TPAO"
url = "https://www.tppd.com.tr/en/oil-prices?id=06"
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = requests.get(url, headers=header)
page_soup = soup(req.content.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
district = page_soup.find_all('td', {"data-title":"DISTRICT"})[0].text.strip()
fuel_price = page_soup.find_all('td', {"data-title":"UNLEADED GASOLINE (TL/LT)"})[0].text.strip()
diesel_price = page_soup.find_all('td', {"data-title":"TP DIESEL (TL/LT)"})[0].text.strip()
lpg_price = page_soup.find_all('td', {"data-title":"TPGAS"})[0].text.strip()

def main():
    FuelTr_update(today,company,district,fuel_price,diesel_price,lpg_price)

if __name__ == "__main__":
    main()