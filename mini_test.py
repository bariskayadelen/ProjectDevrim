# import sqlite3

# def show_all_electric_car_brands():
#     con = sqlite3.connect("car.db")
#     cursor = con.cursor()
#     cursor.execute("SELECT DISTINCT(CarBrand) FROM ElectricCar")
#     data = cursor.fetchall()
#     dict_brand = {}
#     count = 1
#     for i in data:
#         dict_brand[count] = i[0]
#         # print(f" {i[0]}")
#     con.close()
#     # print(f"\n ID\tMarka")
#     # print(f" {'':-^{5}}  {'':-^{10}}")
#     return dict_brand


# print(show_all_electric_car_brands())

list_menu = {
    1:'Area', 
    2:'Fuel Consumption', 
    3:'Length', 
    4:'Temperature', 
    5:'Weight', 
    6:'Volume'}
def menu_main(unit):
    return list_menu[unit]

print(list_menu)
print(menu_main(3))