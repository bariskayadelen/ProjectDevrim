# Import system and name from os for clear function
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
tbl_len_car = 30

def menu_main():
    print(f"\n{' Araç Enerji Tüketimi Hesaplama Programı ':=^{tbl_len_out}}")
    print(f"\nLütfen yapmak istediğiniz işlemi aşağıdaki menüden seçiniz:\n")
    print(f" [11] Araç şarj maliyeti hesapla")
    print(f" [12] Araç tüketim bilgisi hesapla")
    print(f"\n [21] Araç bilgisi göster")
    print(f" [22] Tüm araçların bilgisini göster")
    print(f"\n [31] Güncel akaryakıt fiyatlarını göster")
    print(f" [32] Geçmiş akaryakıt fiyatlarını göster")
    print(f"\n [41] Güncel elektrik fiyatlarını göster")
    print(f"\n{'':-^{tbl_len_out}}")

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
    print(f"\n Güncel elektrik fiyatları aşağıdadır.")
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

def menu_ElectricityTr():
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricityTr")
    data = cursor.fetchall()
    con.close()
    return data[0] 

def ElectricityTr_finder(inp_id):
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricityTr WHERE SubscriptionID=?", (inp_id,))
    data = cursor.fetchall()
    con.close()
    return data[0] 

def ElectricityTr_cost(power,elec_price,dist_price):
    active_energy_cost = power * elec_price
    dist_energy_cost = power * dist_price
    elec_cons_tax = active_energy_cost * 0.05
    energy_fund = active_energy_cost * 0.007
    pre_vat = (active_energy_cost + dist_energy_cost + elec_cons_tax + energy_fund)
    vat = (pre_vat) * 0.18
    total = pre_vat + vat
    return total

def FuelTr_show_now():
    print(f"\n{' Project Devrim ':=^{tbl_len_out}}")
    print(f"\n Güncel akaryakıt fiyatları aşağıdadır.")
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
    print(f"\n Geçmiş akaryakıt fiyatları aşağıdadır.")
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

def car_brand_list():
    pass

def car_finder(carid):
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricCar WHERE CarID=?", (carid,))
    data = cursor.fetchall()
    con.close()
    return data[0]    

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
    elif inp_mainmenu == "11":
        clear()
        print(f"\n{' Araç Enerji Tüketimi Hesaplama Programı ':=^{tbl_len_out}}")
        inp_menu1 = input(f"\n Şarj maliyetini hesaplamak istediğiniz aracın kodunu giriniz: ")
        car_data = car_finder(inp_menu1)
        # inp_menu2 = (f"\n Elektrik tarifenizi giriniz: ")
        inp_menu2 = input(f"\n Elektrik tarifenizi giriniz: ")
        electricity_data = ElectricityTr_finder(inp_menu2)
        cost_charge100 = round(ElectricityTr_cost(car_data[6],electricity_data[3],electricity_data[4]),2)
        cost_charge2080 = round(cost_charge100 * 0.6, 2)
        print(f"\n {'Marka':{tbl_len_car}}: {car_data[1]}")
        print(f" {'Model':{tbl_len_car}}: {car_data[2]}")
        print(f" {'Motor':{tbl_len_car}}: {car_data[3]}")
        print(f" {'Model yılı':{tbl_len_car}}: {car_data[4]}")
        print(f"\n {'Batarya Kapasitesi':{tbl_len_car}}: {car_data[5]} kWh")
        print(f" {'Kullanılabilir Kapasite':{tbl_len_car}}: {car_data[6]} kWh")
        print(f"\n {'Elektrik Tarifesi':{tbl_len_car}}: {electricity_data[1]} - {electricity_data[2]}")
        print(f"\n {'Tam Şarj Ücreti':{tbl_len_car}}: {cost_charge100} ₺")
        print(f" {'%20-%80 Şarj Ücreti':{tbl_len_car}}: {cost_charge2080} ₺")
        print(f"\n{'':-^{tbl_len_out}}")
        inp_menu3 = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp_menu3.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
            break
        elif inp_menu3 == "A":
            continue
        else:
            last_exit(inp_menu3)

    elif inp_mainmenu == "12":
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

    elif inp_mainmenu == "21":
        clear()
        print(f"\n{' Araç Enerji Tüketimi Hesaplama Programı ':=^{tbl_len_out}}")
        inp_menu1 = input(f"\n Götüntülemek istediğiniz aracın ID kodunu giriniz: ")
        car_data = car_finder(inp_menu1)
        print(f"\n {'Marka':{tbl_len_car}}: {car_data[1]}")
        print(f" {'Model':{tbl_len_car}}: {car_data[2]}")
        print(f" {'Motor':{tbl_len_car}}: {car_data[3]}")
        print(f" {'Model yılı':{tbl_len_car}}: {car_data[4]}")
        print(f"\n {'Batarya Kapasitesi':{tbl_len_car}}: {car_data[5]}kWh")
        print(f" {'Kullanılabilir Kapasite':{tbl_len_car}}: {car_data[6]}kWh")
        print(f"\n {'23°C de Normal Havada':{tbl_len_car}}: ")
        print(f" {'WLTP Menzili Şehiriçi':{tbl_len_car}}: {car_data[7]}km")
        print(f" {'WLTP Menzili Şehirdışı':{tbl_len_car}}: {car_data[8]}km")
        print(f" {'WLTP Menzili Karma':{tbl_len_car}}: {car_data[9]}km")
        print(f"\n {'23°C de Normal Havada':{tbl_len_car}}: ")
        print(f" {'Kullanıcı Menzili Şehiriçi':{tbl_len_car}}: {car_data[10]}km")
        print(f" {'Kullanıcı Menzili Şehirdışı':{tbl_len_car}}: {car_data[11]}km")
        print(f" {'Kullanıcı Menzili Karma':{tbl_len_car}}: {car_data[12]}km")
        inp_menu2 = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if inp_menu2.lower() == "q":
            print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
            break
        elif inp_menu2 == "A":
            continue
        else:
            last_exit(inp_menu2)

    elif inp_mainmenu == "22":
        clear()
        car_show()
        if menu_bottom() == "break": break

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
        ElectricityTr_show()
        if menu_bottom() == "break": break

    else:
        clear()
        last_exit(inp_mainmenu)
    continue
