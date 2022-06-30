# Import system and name from os for clear function
from os import system, name
import sqlite3
from beautifultable import BeautifulTable

def menu_car_brands():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT BrandID, Brand FROM CarBrands ORDER BY Brand")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["Marka ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1]])
    print(table)
    con.close()

# menu_car_brands()

def menu_car_models(inp):
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT CarID, CarBrand, CarModel FROM ElectricCar WHERE CarBrand=? ORDER BY CarModel", (inp,))
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka", "Model"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    con.close()
    for i in data:
        table.rows.append([i[0],i[1],i[2]])
    return(table)
