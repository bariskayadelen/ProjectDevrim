# Import functions
from os import system, name
import sqlite3
from time import sleep
# import datetime
# import time
# import tabulate

# Define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def menu_main():
    print(f"\n{' Project Devrim DB Manager ':=^{tbl_len_out}}")
    print(f"\nLütfen yapmak istediğiniz işlemi aşağıdaki menüden seçiniz:\n")
    print(f" [11] Elektrik fiyat bilgisini göster")
    # print(f" [12] Elektrik fiyat bilgisini ekle")
    # print(f" [13] Elektrik fiyat bilgisini güncelle")
    # print(f" [41] Elektrik fiyat bilgisini sil\n")
    print(f" [21] Su fiyat bilgisini göster")
    # print(f" [22] Su fiyat bilgisini güncelle\n")
    print(f"\n [31] Güncel akaryakıt fiyat bilgisini göster")
    print(f" [32] Tüm akaryakıt fiyat bilgisini göster")
    # print(f" [32] Akaryakıt fiyat bilgisini güncelle\n")
    print(f"\n [41] Tüm araçların bilgisini göster")
    # print(f" [42] Araç bilgisini güncelle")

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
    print(f"\n{' Project Devrim DB Manager ':=^{tbl_len_out}}")
    print(f"\n Hata!!! Girmiş olduğunuz {inp} değeri menüde mevcut değildir.")
    print(f"\n Lütfen menü seçeneğini doğru giriniz!")
    print(f"\n Uyarı: 5 sn sonra ana menüye döneceksiniz.")
    sleep(5)

def ElectricityTr_show():
    print(f"\n{' Project Devrim DB Manager ':=^{tbl_len_out}}")
    print(f"\n Güncel elektrik fiyat bilgisi aşağıdadır.")
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ElectricityTr(SubscriptionID INT,SubscriptionGroup TEXT,SubscriptionTariff TEXT,ElectricityPrice REAL,DistributionPrice REAL)")
    con.commit()
    cursor.execute("SELECT * FROM ElectricityTr")
    data = cursor.fetchall()
    print(f"\n ID\tAbone Grubu\tTarife\t\tTarife Bedeli\tDağıtım Bedeli")
    print(f" {'':-^{5}}  {'':-^{14}}  {'':-^{tbl_len_5c}}   {'':-^{tbl_len_5c}}   {'':-^{tbl_len_5c}}")
    for i in data:
        print(f" [{i[0]}]\t{i[1]}\t\t{i[2]} - {i[3]} - {i[4]}")
    con.close()

# Eksik tamamla !!!
def ElectricityTr_add():
    print(f"\n{' Project Devrim DB Manager ':=^{tbl_len_out}}")
    inp_SubscriptionID = input("")
    pass

def FuelTr_show_now():
    print(f"\n{' Project Devrim ':=^{tbl_len_out}}")
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
    print(f"\n{' Project Devrim DB Manager ':=^{tbl_len_out}}")
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

# Table dimentions
tbl_len_out = 78
tbl_len_in = 38
tbl_len_5c = 13

while True:
    clear()
    menu_main()
    inp_mainmenu = input(f"\n[Q] Programdan Çık | Tercih: ")
    if inp_mainmenu.lower() == "q":
        print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
        break

    elif inp_mainmenu == "11":
        clear()
        ElectricityTr_show()
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
        if menu_bottom() == "break": break

    # elif inp_mainmenu == "22":
    #     clear()
    #     under_construction()
    #     if menu_bottom() == "break": break

    elif inp_mainmenu == "31":
        clear()
        FuelTr_show_now()
        if menu_bottom() == "break": break

    elif inp_mainmenu == "32":
        clear()
        FuelTr_show_all()
        if menu_bottom() == "break": break

    elif inp_mainmenu == "41":
        clear()
        car_show()
        if menu_bottom() == "break": break

    # elif inp_mainmenu == "42":
    #     clear()
    #     under_construction()
    #     if menu_bottom() == "break": break

    else:
        clear()
        last_exit(inp_mainmenu)
    continue