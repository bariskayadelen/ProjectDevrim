# Fuel Price Watcher Script

from datetime import datetime
from  get_fuelprice_tr import fuel_company, fuel_price, diesel_price, lpg_price
import sqlite3

# now = datetime.now()
today = str(datetime.today().strftime('%Y-%m-%d'))

def FuelTr_update(today,comp,fuel,diesel,lpg):
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS FuelTr(Date TEXT,CompanyName TEXT,GasPrice REAL,Diesel REAL,LPG REAL)")
    con.commit()
    data = cursor.execute("SELECT * FROM FuelTr ORDER BY Date DESC LIMIT 1")
    data = cursor.fetchone()[0]
    if data == today:
        print ("Bugün için veri girişi yapılmış.")
    else:
        insert_with_param = """INSERT INTO FuelTr (Date,CompanyName,GasPrice,Diesel,LPG) VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (today,comp,fuel,diesel,lpg)
        cursor.execute(insert_with_param, data_tuple)
        con.commit()
        print ("Yeni veri girişi yapıldı.")
    con.close()

def main():
    FuelTr_update(today,fuel_company,fuel_price,diesel_price,lpg_price)

if __name__ == "__main__":
    main()
