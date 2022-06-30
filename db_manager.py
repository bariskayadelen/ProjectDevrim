# Import functions
from os import system, name
import sqlite3
from time import sleep
from beautifultable import BeautifulTable

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def menu_title():
    return (f"\n{' Project Devrim DB Manager ':=^{tbl_len_out}}")

def menu_main():
    print(menu_title())
    print(f"\nLütfen yapmak istediğiniz işlemi aşağıdaki menüden seçiniz:\n")
    print(f" [11] Elektrik fiyat bilgisini göster")
    # print(f" [12] Elektrik fiyat bilgisini ekle")
    # print(f" [13] Elektrik fiyat bilgisini güncelle")
    # print(f" [41] Elektrik fiyat bilgisini sil\n")
    print(f"\n [21] Su fiyat bilgisini göster")
    # print(f" [22] Su fiyat bilgisini güncelle\n")
    print(f"\n [31] Güncel akaryakıt fiyat bilgisini göster")
    print(f" [32] Tüm akaryakıt fiyat bilgisini göster")
    print(f"\n [41] Tüm araçların bilgisini göster")
    # print(f" [42] Araç bilgisini güncelle")
    print(f"\n [51] Elektrikli araç markalarını göster")
    print(f" [52] Elektrikli araç markalarının veritabanını güncelle")
    print(f" [53] Hibrit araç markalarını göster")
    print(f" [54] Hibrit araç markalarının veritabanını güncelle")
    print(f" [55] Benzinli/Dizel araç markalarını göster")
    print(f" [56] Benzinli/Dizel araç markaları veritabanını güncelle")

def menu_bottom():
    while True:
        inp = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
            return "break"
        elif inp.lower() == "a":
            return "continue"
        else:
            clear()
            print(menu_title())
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri menüde mevcut değildir.")
            print(f"\n Lütfen menü seçeneğini doğru giriniz!")
            print(f"\n{'':-^{tbl_len_out}}")
        continue

def menu_error(inp):
    print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri menüde mevcut değildir.")
    print(f"\n Lütfen menü seçeneğini doğru giriniz!")

def last_exit(inp):
    print(menu_title())
    print(f"\n Hata!!! Girmiş olduğunuz {inp} değeri menüde mevcut değildir.")
    print(f"\n Lütfen menü seçeneğini doğru giriniz!")
    print(f"\n Uyarı: 5 sn sonra ana menüye döneceksiniz.")
    sleep(5)

def show_all_ElectricityTr():
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricityTr")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Abone Grubu", "Tarife", "Tarife Bed.", "Dağ. Bed."]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1],i[2],i[3],i[4]])
    print(table)
    con.close()

# Eksik tamamla !!!
def ElectricityTr_add():
    print(menu_title())
    inp_SubscriptionID = input("")
    pass

def FuelTr_show_now():
    print(menu_title())
    print(f"\n Güncel akaryakıt fiyat bilgisi aşağıdadır.")
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM FuelTr ORDER BY Date DESC LIMIT 1")
    data = cursor.fetchall()
    print(f"\n Tarih  \tŞirket  \tBenzin Fiyatı\tDizel Fiyatı\tLPG Fiyatı")
    print(f" {'':-^{13}}  {'':-^{13}}   {'':-^{13}}   {'':-^{13}}   {'':-^{13}}")
    for i in data:
        print(f" {i[0]}\t{i[1]}\t{i[2]}\t\t{i[3]}\t\t{i[4]}")
    con.close()

def FuelTr_show_all():
    print(menu_title())
    print(f"\n Güncel akaryakıt fiyat bilgisi aşağıdadır.")
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM FuelTr")
    data = cursor.fetchall()
    print(f"\n Tarih  \tŞirket  \tBenzin Fiyatı\tDizel Fiyatı\tLPG Fiyatı")
    print(f" {'':-^{13}}  {'':-^{13}}   {'':-^{13}}   {'':-^{13}}   {'':-^{13}}")
    for i in data:
        print(f" {i[0]}\t{i[1]}\t{i[2]}\t\t{i[3]}\t\t{i[4]}")
    con.close()

def car_show():
    # https://ev-database.org/
    print(menu_title())
    print(f"\n Tüm araçlara ait bilgiler aşağıdadır.")
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ElectricCar(CarID INT,CarBrand TEXT,CarModel TEXT,EngineModel TEXT,ModelYear INT,BatteryCapacity REAL,UseableCapacity REAL,WLTPRangeCity REAL,WLTPRangeHighway REAL,WLTPRangeCombine REAL,RealRangeCity REAL,RealRangeHighway REAL,RealRangeCombine REAL)")
    con.commit()
    cursor.execute("SELECT * FROM ElectricCar")
    data = cursor.fetchall()
    print(f"\n ID\tMarka\tModel\t\tMotor\t\tYıl\tPil Kap.\tKul. Pil\tWLTP Menzili.\tKul. Menzili")
    print(f" {'':-^{5}}  {'':-^{6}}  {'':-^{14}}  {'':-^{14}}  {'':-^{6}}  {'':-^{14}}  {'':-^{14}}  {'':-^{14}}  {'':-^{14}}")
    for i in data:
        print(f" {i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t\t{i[4]}\t{i[5]}kWh\t\t{i[6]}kWh\t\t{i[9]}km\t\t{i[12]}km")
    con.close()

# def show_all_electric_car_brands():
#     con = sqlite3.connect("car.db")
#     cursor = con.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS CarBrands(BrandID INT,CarBrand TEXT, CarModels)")
#     con.commit()
#     cursor.execute("SELECT * FROM CarBrands")
#     data = cursor.fetchall()

#     print(f"\n ID\tBrand")
#     print(f" {'':-^{5}}  {'':-^{10}}")
#     for i in data:
#         print(f" {i[0]}")
#     con.close()

def show_ElectricCarBrands():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ElectricCarBrands (BrandID INTEGER PRIMARY KEY,Brand TEXT NOT NULL)")
    con.commit()
    cursor.execute("SELECT * FROM ElectricCarBrands")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["Marka ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    con.close()
    for i in data:
        table.rows.append([i[0],i[1]])
    return(table)
# print(show_ElectricCarBrands())

def show_FuelCarBrands():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS FuelCarBrands (BrandID INTEGER PRIMARY KEY,Brand TEXT NOT NULL)")
    con.commit()
    cursor.execute("SELECT * FROM FuelCarBrands")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    con.close()
    for i in data:
        table.rows.append([i[0],i[1]])
    return(table)
# print(show_FuelCarBrands())

def show_HybridCarBrands():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS HybridCarBrands (BrandID INTEGER PRIMARY KEY,Brand TEXT NOT NULL)")
    con.commit()
    cursor.execute("SELECT * FROM HybridCarBrands")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    con.close()
    for i in data:
        table.rows.append([i[0],i[1]])
    return(table)
# print(show_HybridCarBrands())

def under_construction():
    print(menu_title())
    print(f"\n Bu modül yapım aşamasındadır.")

def update_ElectricCarBrands():
    # Read Cars Brands from ElectricCar table
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT(CarBrand) FROM ElectricCar ORDER BY CarBrand")
    data_cars = cursor.fetchall()
    # Clean previous table data
    cursor.execute("DELETE FROM ElectricCarBrands")
    # Update Car Brands on ElectricCarBrands table
    for carbrand in data_cars:
        cursor.execute("INSERT INTO ElectricCarBrands (Brand) VALUES (?)", (carbrand))
    con.commit()
    # Print Car Brands from ElectricCarBrands table
    cursor.execute("SELECT * FROM ElectricCarBrands")
    data_brands = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["Marka ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    con.close()
    for i in data_brands:
        table.rows.append([i[0],i[1]])
    return(table)
# print(update_ElectricCarBrands())

def update_FuelCarBrands():
    # Read Cars Brands from FuelCar table
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT(CarBrand) FROM FuelCar ORDER BY CarBrand")
    data_cars = cursor.fetchall()
    # Clean previous table data
    cursor.execute("DELETE FROM FuelCarBrands")
    # Update Car Brands on FuelCarBrands table
    for carbrand in data_cars:
        cursor.execute("INSERT INTO FuelCarBrands (Brand) VALUES (?)", (carbrand))
    con.commit()
    # Print Car Brands from FuelCarBrands table
    cursor.execute("SELECT * FROM FuelCarBrands")
    data_brands = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    con.close()
    for i in data_brands:
        table.rows.append([i[0],i[1]])
    return(table)
# print(update_FuelCarBrands())

def update_HybridCarBrands():
    # Read Cars Brands from HybridCar table
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT(CarBrand) FROM HybridCar ORDER BY CarBrand")
    data_cars = cursor.fetchall()
    # Clean previous table data
    cursor.execute("DELETE FROM HybridCarBrands")
    # Update Car Brands on HybridCarBrands table
    for carbrand in data_cars:
        cursor.execute("INSERT INTO HybridCarBrands (Brand) VALUES (?)", (carbrand))
    con.commit()
    # Print Car Brands from HybridCarBrands table
    cursor.execute("SELECT * FROM HybridCarBrands")
    data_brands = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    con.close()
    for i in data_brands:
        table.rows.append([i[0],i[1]])
    return(table)
# print(update_HybridCarBrands())

# Table dimentions
tbl_len_out = 78
tbl_len_in = 38
tbl_len_5c = 13

update_ElectricCarBrands()
update_FuelCarBrands()

while True:
    clear()
    menu_main()
    print(f"\n{'':-^{tbl_len_out}}")
    inp_mainmenu = input(f"\n[Q] Programdan Çık | Tercih: ")
    if inp_mainmenu.lower() == "q":
        print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
        break

    elif inp_mainmenu == "11":
        clear()
        print(menu_title())
        print(f"\n Güncel elektrik fiyatları aşağıdadır.\n")
        show_all_ElectricityTr()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # elif inp_mainmenu == "12":
    #     clear()
    #     ElectricityTr_add()
    #     if menu_bottom() == "break": break

    # elif inp_mainmenu == "13":
    #     clear()
    #     under_construction()
    #     if menu_bottom() == "break": break

    # elif inp_mainmenu == "14":
    #     clear()
    #     under_construction()
    #     if menu_bottom() == "break": break

    elif inp_mainmenu == "21":
        clear()
        under_construction()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # elif inp_mainmenu == "22":
    #     clear()
    #     under_construction()
    #     if menu_bottom() == "break": break

    elif inp_mainmenu == "31":
        clear()
        FuelTr_show_now()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    elif inp_mainmenu == "32":
        clear()
        FuelTr_show_all()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    elif inp_mainmenu == "41":
        clear()
        car_show()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # elif inp_mainmenu == "42":
    #     clear()
    #     print(menu_title())
    #     under_construction()
    #     print(f"\n{'':-^{tbl_len_out}}")
    #     if menu_bottom() == "break": break

    # Show electric car brands
    elif inp_mainmenu == "51":
        clear()
        print(menu_title())
        print("")
        print(show_ElectricCarBrands())
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # Update electric car brands table
    elif inp_mainmenu == "52":
        clear()
        print(menu_title())
        print("")
        print(update_ElectricCarBrands())
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # Show hybrid car brands
    # elif inp_mainmenu == "53":
    #     clear()
    #     print(menu_title())
    #     print("")
    #     print(show_HybridCarBrands())
    #     print(f"\n{'':-^{tbl_len_out}}")
    #     if menu_bottom() == "break": break

    # Update hybrid car brands table
    # elif inp_mainmenu == "54":
    #     clear()
    #     print(menu_title())
    #     print("")
    #     print(update_HybridCarBrands())
    #     print(f"\n{'':-^{tbl_len_out}}")
    #     if menu_bottom() == "break": break

    # Show fuel car brands
    elif inp_mainmenu == "55":
        clear()
        print(menu_title())
        print("")
        print(show_FuelCarBrands())
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # Update fuel car brands table
    elif inp_mainmenu == "56":
        clear()
        print(menu_title())
        print("")
        print(update_FuelCarBrands())
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    else:
        clear()
        print(menu_title())
        menu_error(inp_mainmenu)
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break
    continue
