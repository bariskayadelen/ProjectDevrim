# Import system and name from os for clear function
from os import system, name
# from time import sleep
import sqlite3

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def menu_title():
    return (f"\n{' Araç Enerji Tüketimi Hesaplama Programı ':=^{tbl_len_out}}")

def menu_main():
    print(menu_title())
    print(f"\nLütfen yapmak istediğiniz işlemi aşağıdaki menüden seçiniz:\n")
    print(f" [11] Elektrikli araç şarj maliyeti hesapla")
    print(f" [12] Hibrit araç şarj/depo dolum maliyeti hesapla")
    print(f" [13] Benzinli/Dizel araç depo dolum maliyeti hesapla")
    print(f"\n [21] Araç bilgisi göster")
    print(f" [22] Tüm araçların bilgisini göster")
    print(f"\n [31] Güncel akaryakıt fiyatlarını göster")
    print(f" [32] Geçmiş akaryakıt fiyatlarını göster")
    print(f"\n [41] Güncel elektrik fiyatlarını göster")
    print(f"\n{'':-^{tbl_len_out}}")

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

def menu_car_electric():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricCar")
    data = cursor.fetchall()
    print(f"\n ID\tMarka\t\tModel")
    print(f" {'':-^{5}}  {'':-^{14}}  {'':-^{30}}")
    for i in data:
        print(f" {i[0]}\t{i[1]}\t\t{i[2]}")
    con.close()

def find_electric_car(carid):
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricCar WHERE CarID=?", (carid,))
    data = cursor.fetchall()
    con.close()
    return data[0]

def find_electric_car_brand():
    pass    

def show_all_cars():
    # https://ev-database.org/
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricCar")
    data = cursor.fetchall()
    print(f"\n ID\tMarka\tModel\t\tMotor\t\tYıl\tPil Kap.\tKul. Pil\tWLTP Menzili.\tKul. Menzili")
    print(f" {'':-^{5}}  {'':-^{6}}  {'':-^{14}}  {'':-^{14}}  {'':-^{6}}  {'':-^{14}}  {'':-^{14}}  {'':-^{14}}  {'':-^{14}}")
    for i in data:
        print(f" {i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t\t{i[4]}\t{i[5]}kWh\t\t{i[6]}kWh\t\t{i[9]}km\t\t{i[12]}km")
    con.close()

# !!! 
def show_all_electric_car_brands():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT(CarBrand) FROM ElectricCar")
    data = cursor.fetchall()

    print(f"\n ID\tMarka")
    print(f" {'':-^{5}}  {'':-^{10}}")
    for i in data:
        print(f" {i[0]}")
    con.close()

# !!! 
def show_all_hibrid_car_brands():
    pass

# !!! 
def show_all_gasoline_car_brands():
    pass


def show_current_FuelTr():
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM FuelTr ORDER BY Date DESC LIMIT 1")
    data = cursor.fetchall()
    print(f"\n Tarih  \tŞirket  \tBenzin Fiyatı\tDizel Fiyatı\tLPG Fiyatı")
    print(f" {'':-^{13}}  {'':-^{13}}   {'':-^{13}}   {'':-^{13}}   {'':-^{13}}")
    for i in data:
        print(f" {i[0]}\t{i[1]}\t{i[2]}\t\t{i[3]}\t\t{i[4]}")
    con.close()

def show_all_FuelTr():
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM FuelTr")
    data = cursor.fetchall()
    print(f"\n Tarih  \tŞirket  \tBenzin Fiyatı\tDizel Fiyatı\tLPG Fiyatı")
    print(f" {'':-^{13}}  {'':-^{13}}   {'':-^{13}}   {'':-^{13}}   {'':-^{13}}")
    for i in data:
        print(f" {i[0]}\t{i[1]}\t{i[2]}\t\t{i[3]}\t\t{i[4]}")
    con.close()

def show_all_ElectricityTr():
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricityTr")
    data = cursor.fetchall()
    print(f"\n ID\tAbone Grubu\tTarife\t\tTarife Bedeli\tDağıtım Bedeli")
    print(f" {'':-^{5}}  {'':-^{14}}  {'':-^{13}}   {'':-^{13}}   {'':-^{13}}")
    for i in data:
        print(f" {i[0]}\t{i[1]}\t\t{i[2]} - {i[3]} - {i[4]}")
    con.close()

def under_construction():
    print(f"\n Bu modül yapım aşamasındadır.")

# Table dimentions
tbl_len_out = 78
tbl_len_in = 38
tbl_len_car = 30

while True:
    clear()
    menu_main()
    inp_mainmenu = input(f"\n[Q] Programdan Çık | Tercih: ")
    if inp_mainmenu.lower() == "q":
        print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
        break

    # [11] Elektrikli araç şarj maliyeti hesapla
    elif inp_mainmenu == "11":
        clear()
        print(menu_title())
        print(f"\n Şarj maliyetini hesaplamak istediğiniz aracın markasını giriniz: ")
        under_construction()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [12] Hibrit araç şarj/depo dolum maliyeti
    elif inp_mainmenu == "12":
        clear()
        print(menu_title())
        under_construction()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [13] Benzinli/Dizel araç depo dolum maliyeti hesapla
    elif inp_mainmenu == "13":
        clear()
        print(menu_title())
        under_construction()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [21] Araç bilgisi
    elif inp_mainmenu == "21":
        clear()
        print(menu_title())
        print(f"\n Görüntülemek istediğiniz araç türünü seçiniz ")
        print("\n [1] Elektrikli araç")
        print(" [2] Hibrit araç")
        print(" [3] Benzinli/Diesel araç")
        print(f"\n{'':-^{tbl_len_out}}")
        inp_menu21 = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp_menu21.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
            break
        elif inp_menu21.lower() == "a":
            continue
        elif inp_menu21 == "1":
            clear()
            print(menu_title())
            print(f"\n Görüntülemek istediğiniz araç narkasini seçiniz ")
            show_all_electric_car_brands()
            under_construction()
            print(f"\n{'':-^{tbl_len_out}}")
            if menu_bottom() == "break": break
        elif inp_menu21 == "2":
            clear()
            print(menu_title())
            under_construction()
            print(f"\n{'':-^{tbl_len_out}}")
            if menu_bottom() == "break": break
        elif inp_menu21 == "3":
            clear()
            print(menu_title())
            under_construction()
            print(f"\n{'':-^{tbl_len_out}}")
            if menu_bottom() == "break": break
        else:
            clear()
            print(menu_title())
            menu_error(inp_menu21)
            print(f"\n{'':-^{tbl_len_out}}")
            if menu_bottom() == "break": break

    # [22] Tüm araçların bilgisi
    elif inp_mainmenu == "22":
        clear()
        print(menu_title())
        print(f"\n Tüm araçlara ait bilgiler aşağıdadır.")
        show_all_cars()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [31] Güncel akaryakıt fiyatları
    elif inp_mainmenu == "31":
        clear()
        print(menu_title())
        print(f"\n Güncel akaryakıt fiyatları aşağıdadır.")
        show_current_FuelTr()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [32] Geçmiş akaryakıt fiyatları
    elif inp_mainmenu == "32":
        clear()
        print(menu_title())
        print(f"\n Geçmiş akaryakıt fiyatları aşağıdadır.")
        show_all_FuelTr()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [41] Güncel elektrik fiyatları
    elif inp_mainmenu == "41":
        clear()
        print(menu_title())
        print(f"\n Güncel elektrik fiyatları aşağıdadır.")
        show_all_ElectricityTr()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    else:
        clear()
        print(menu_title())
        menu_error(inp_mainmenu)
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break
    continue
