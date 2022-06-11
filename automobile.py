# Import system and name from os for clear function
from operator import eq
from os import system, name
from time import sleep
import sqlite3

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Table dimentions
tbl_len_out = 78
tbl_len_in = 38

def menu_main():
    print(f"\n{' Araç Enerji Tüketimi Hesaplama Programı ':=^{tbl_len_out}}")
    print(f"\nLütfen yapmak istediğiniz işlemi aşağıdaki menüden seçiniz:\n")
    print(f" [1] Araç tüketim bilgisi hesapla")
    print(f" [2] Tüm araçların bilgisini göster")
    print(f" [3] Akaryakıt fiyat bilgisini göster")
    print(f" [4] Elektrik fiyat bilgisini göster")

def menu_bottom():
    inp = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
    if inp.lower() == "q":
        print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
        return "break"
    elif inp.lower() == "a":
        return "continue"
    else:
        last_exit(inp)

def last_exit(inp):
    print(f"\n{' Project Devrim ':=^{tbl_len_out}}")
    print(f"\n Hata!!! Girmiş olduğunuz {inp} değeri menüde mevcut değildir.")
    print(f"\n Lütfen menü seçeneğini doğru giriniz!")
    print(f"\n Uyarı: 5 sn sonra ana menüye döneceksiniz.")
    sleep(5)

def ElectricityTr_show():
    print(f"\n{' Project Devrim ':=^{tbl_len_out}}")
    print(f"\n Güncel elektrik fiyat bilgisi aşağıdadır.")
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ElectricityTr(SubscriptionID INT,SubscriptionGroup TEXT,SubscriptionTariff TEXT,ElectricityPrice REAL,DistributionPrice REAL)")
    con.commit()
    cursor.execute("SELECT * FROM ElectricityTr")
    data = cursor.fetchall()
    print(f"\n ID\tAbone Grubu\tTarife\t\tTarife Bedeli\tDağıtım Bedeli")
    print(f" {'':-^{5}}  {'':-^{14}}  {'':-^{13}}   {'':-^{13}}   {'':-^{13}}")
    for i in data:
        print(f" [{i[0]}]\t{i[1]}\t\t{i[2]} - {i[3]} - {i[4]}")
    con.close()

def FuelTr_show():
    print(f"\n{' Project Devrim ':=^{tbl_len_out}}")
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
    print(f"\n{' Project Devrim ':=^{tbl_len_out}}")
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

def under_construction():
    print(f"\n{' Project Devrim DB Manager ':=^{tbl_len_out}}")
    print(f"\n Bu modül yapım aşamasındadır.")

while True:
    clear()
    menu_main()
    # inp_mainmenu = input(f"\n{' [Q] Programdan Çık ':{tbl_len_in}}  {'  ':{tbl_len_in}} \n\nSeçenek: ")
    inp_mainmenu = None
    inp_mainmenu = input(f"\n[Q] Programdan Çık | Tercih: ")
    if inp_mainmenu.lower() == "q":
        print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
        break
    elif inp_mainmenu == "1":
        clear()
        print(f"\n{' Araç Enerji Tüketimi Hesaplama Programı ':=^{tbl_len_out}}")
        print(f"\n Hesaplama yapmak istediğiniz araç markasını seçiniz:")
        print(f"\n [1] Audi     [2] BMW     [3] Citroen [4] DS      [5] Hyundai [6] Jaguar")
        print(f" [7] Mercedes [8] Mini    [9] Nissan  [10] Peugeot[11] Toyota [12] Polestar")
        print(f" [13] Porsche [14] Renault[15] Skoda  [16] Smart  [17] Tesla   [18] Volkswagen")
        print(f" [19] Volvo")
        inp_menu1 = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp_menu1.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
            break
        elif inp_menu1 == "A":
            continue
        else:
            last_exit(inp_menu1)
    elif inp_mainmenu == "2":
        clear()
        car_show()
        if menu_bottom() == "break": break

    elif inp_mainmenu == "3":
        clear()
        FuelTr_show()
        if menu_bottom() == "break": break

    elif inp_mainmenu == "4":
        clear()
        FuelTr_show()
        if menu_bottom() == "break": break

    else:
        clear()
        last_exit(inp_mainmenu)
    continue
