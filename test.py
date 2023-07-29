# Import system and name from os for clear function
from os import system, name
import sqlite3
from beautifultable import BeautifulTable

def calc_fuel_cost(fuel_type,tank_size):
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM FuelTr ORDER BY Date DESC LIMIT 1")
    data = cursor.fetchall()
    for i in data:
        if fuel_type == "Benzin":
            return(int(i[2]) * tank_size)
        elif fuel_type == "Diesel":
            return(int(i[3]) * tank_size)
        elif fuel_type == "LPG":
            return(int(i[4]) * tank_size)
        else:
            return None
    con.close()

fuel_cost = calc_fuel_cost("Benzin",54.0)

print(fuel_cost)

