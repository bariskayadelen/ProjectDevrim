# Import system and name from os for clear function
from os import system, name
import sqlite3
from beautifultable import BeautifulTable

# def menu_car_electric():
#     con = sqlite3.connect("car.db")
#     cursor = con.cursor()
#     cursor.execute("SELECT DISTINCT CarBrand FROM ElectricCar ORDER BY CarBrand")
#     data = cursor.fetchall()
#     table = BeautifulTable()
#     table.set_style(BeautifulTable.STYLE_COMPACT)
#     table.columns.header = ["Marka"]
#     table.columns.alignment = BeautifulTable.ALIGN_LEFT
#     for i in data:
#         table.rows.append([i[0]])
#     print(table)
#     con.close()
#     # return (data)

# # print(menu_car_electric())
# menu_car_electric()




def menu_car_brands():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    # cursor.execute("SELECT BrandID, Brand FROM CarBrands WHERE Emodel IN (1)")
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

menu_car_brands()

def menu_car_models(inp):
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    # cursor.execute("SELECT BrandID, Brand FROM CarBrands WHERE Emodel IN (1)")
    cursor.execute("SELECT CarBrand, CarModel FROM ElectricCar WHERE CarBrand=? ORDER BY CarModel", (inp,))
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["Marka ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1]])
    print(table)
    con.close()

menu_car_models('Tesla')
