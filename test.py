# Web sayfasından otomatik akaryakıt fiyatlarını alan script

import datetime
import urllib.request
from bs4 import BeautifulSoup as soup
import sqlite3

# def FuelTr_show():
#     con = sqlite3.connect("unitprices.db")
#     cursor = con.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS FuelTr(Date TEXT,CompanyName TEXT,GasPrice REAL,Diesel REAL,LPG REAL)")
#     con.commit()
#     cursor.execute("SELECT * FROM FuelTr")
#     data = cursor.fetchall()
#     print(f"\n Tarih  \tŞirket  \tBenzin Fiyatı\tDizel Fiyatı\tLPG Fiyatı")
#     for i in data:
#         print(f" {i[0]}\t{i[1]}\t{i[2]}\t\t{i[3]}\t\t{i[4]}")
#     con.close()

def FuelTr_update(date,comp,fuel,diesel,lpg):
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS FuelTr(Date TEXT,CompanyName TEXT,GasPrice REAL,Diesel REAL,LPG REAL)")
    con.commit()
    cursor.execute("SELECT * FROM FuelTr")
    data = cursor.fetchall()
    for i in data:
        if i[0] == today:
            print ("Bugun veri girisi yapilmis.")
        else:
            # print(f" {date}\t{comp}\t{fuel}\t\t{diesel}\t\t{lpg}")
            # cursor.execute("INSERT INTO FuelTr (Date,CompanyName,GasPrice,Diesel,LPG) VALUES(date,comp,fuel,diesel,lpg)")
            insert_with_param = """INSERT INTO FuelTr (Date,CompanyName,GasPrice,Diesel,LPG) VALUES (?, ?, ?, ?, ?);"""
            data_tuple = (date,comp,fuel,diesel,lpg)
            cursor.execute(insert_with_param, data_tuple)
            con.commit()
    con.close()

today = datetime.date.today()
url = "https://www.aytemiz.com.tr/"
company = "Aytemiz Petrol"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
uClient = urllib.request.urlopen(req)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
fuel_price = page_soup.find_all('div', {"class":"fuel-price"})[0].text.strip().strip('TL/LT')
diesel_price = page_soup.find_all('div', {"class":"fuel-price"})[1].text.strip().strip('TL/LT')
lpg_price = page_soup.find_all('div', {"class":"fuel-price"})[3].text.strip().strip('TL/LT')

FuelTr_update(today,company,fuel_price,diesel_price,lpg_price)
