# Import system and name from os for clear function
from os import system, name
import sqlite3
from beautifultable import BeautifulTable

def menu_car_electric():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT CarID, CarBrand, CarModel, EngineModel FROM ElectricCar ORDER BY CarBrand, CarModel")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka", "Model", "Motor"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1],i[2],i[3]])
    print(table)
    con.close()
    # return (data)

# print(menu_car_electric())
menu_car_electric()
