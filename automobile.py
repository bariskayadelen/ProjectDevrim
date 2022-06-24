# Import system and name from os for clear function
from os import system, name
import sqlite3
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

def menu_ElectricityTr():
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricityTr")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Abone Grubu", "Tarife"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1],i[2]])
    print(table)
    con.close()

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

def menu_car_fuel():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT CarID, CarBrand, CarModel, EngineModel FROM FuelCar ORDER BY CarBrand, CarModel")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka", "Model", "Motor"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1],i[2],i[3]])
    print(table)
    con.close()

def menu_car_brands():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT BrandID, Brand FROM CarBrands WHERE Emodel ='1' ORDER BY Brand")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1]])
    return(table)
    con.close()

def calc_ElectricityTr(power,elec_price,dist_price):
    active_energy_cost = power * elec_price
    dist_energy_cost = power * dist_price
    elec_cons_tax = active_energy_cost * 0.05
    energy_fund = active_energy_cost * 0.007
    pre_vat = (active_energy_cost + dist_energy_cost + elec_cons_tax + energy_fund)
    vat = (pre_vat) * 0.18
    total = pre_vat + vat
    return total

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

def calc_fuel_cost_per_km(fuel_type,consumption):
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM FuelTr ORDER BY Date DESC LIMIT 1")
    data = cursor.fetchall()
    for i in data:
        if fuel_type == "Benzin":
            return(int(i[2]) * consumption / 100)
        elif fuel_type == "Diesel":
            return(int(i[3]) * consumption / 100)
        elif fuel_type == "LPG":
            return(int(i[4]) * consumption / 100)
        else:
            return None
    con.close()

def calc_row_number(inp):
    if inp == "ElectricityTr":
        con = sqlite3.connect("unitprices.db")
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM ElectricityTr")
        row_number = cursor.fetchone()[0]
        return row_number
    elif inp == "ElectricCar":
        con = sqlite3.connect("car.db")
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM ElectricCar")
        row_number = cursor.fetchone()[0]
        return row_number
    elif inp == "FuelCar":
        con = sqlite3.connect("car.db")
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*) FROM FuelCar")
        row_number = cursor.fetchone()[0]
        return row_number
    else:
        return "0"

def find_ElectricityTr(inp):
    while True:
        try:
            inp_id = float(inp)
            con = sqlite3.connect("unitprices.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM ElectricityTr WHERE SubscriptionID=?", (inp_id,))
            data = cursor.fetchall()
            con.close()
            return data[0]
        except:
            clear()
            print(menu_title())
            menu_ElectricityTr()
            print(f"\n Hata!!! Girmiş olduğunuz '{inp}' değeri menüde mevcut değildir.")
            print(f"\n Lütfen menü seçeneğini doğru giriniz!")
            inp = input(f"\n Şarj maliyetini hesaplamak istediğiniz aracın kodunu giriniz: ")
            continue

def find_electric_car(carid):
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricCar WHERE CarID=?", (carid,))
    data = cursor.fetchall()
    con.close()
    return data[0]

def find_electric_car_brand():
    pass

# https://motoreu.com/
def find_fuel_car(carid):
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM FuelCar WHERE CarID=?", (carid,))
    data = cursor.fetchall()
    con.close()
    return data[0]

# https://ev-database.org/
def show_all_cars():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ElectricCar")
    data = cursor.fetchall()
    table = BeautifulTable(maxwidth=118)
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["ID", "Marka", "Model", "Motor", "Yıl", "Pil Kap.", "Kul. Pil", "WLTP Menzili", "Kul. Menzili"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    # table.rows.append[("","","","","","kWh","kWh","km","km")]
    for i in data:
        table.rows.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[9],i[12]])
    print(table)
    con.close()

# !!! 
def show_all_electric_car_brands():
    con = sqlite3.connect("car.db")
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT(CarBrand) FROM ElectricCar")
    data = cursor.fetchall()
    dict_brand = []
    count = 0
    print(f"\n ID\tMarka")
    print(f" {'':-^{5}}  {'':-^{10}}")
    for i in data:
        dict_brand.append(count, {i[0]})
        # print(f" {i[0]}")
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
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["Tarih", "Şirket", "Benzin Fiyatı", "Dizel Fiyatı", "LPG Fiyatı"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1],i[2],i[3],i[4]])
    print(table)
    con.close()

def show_all_FuelTr():
    con = sqlite3.connect("unitprices.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM FuelTr")
    data = cursor.fetchall()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.columns.header = ["Tarih", "Şirket", "Benzin Fiyatı", "Dizel Fiyatı", "LPG Fiyatı"]
    table.columns.alignment = BeautifulTable.ALIGN_LEFT
    for i in data:
        table.rows.append([i[0],i[1],i[2],i[3],i[4]])
    print(table)
    con.close()

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

def under_construction():
    print(f"\n Bu modül yapım aşamasındadır.")

# Table dimentions
tbl_len_out = 98
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
        print(f"\n Şarj maliyetini hesaplamak istediğiniz aracın ID kodunu giriniz.\n")
        menu_car_electric()
        print(f"\n{'':-^{tbl_len_out}}")
        inp_menu11 = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        try:
            menu11 = int(inp_menu11)
            if menu11 in range(1,(calc_row_number("ElectricCar") + 1)):
                car_data = find_electric_car(inp_menu11)
                clear()
                print(menu_title())
                print(f"\n Şarj maliyetini hesaplamak istediğiniz elektrik tarifesini giriniz.\n")
                menu_ElectricityTr()
                print(f"\n{'':-^{tbl_len_out}}")
                inp_menu111 = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
                try:
                    menu111 = int(inp_menu111)
                    if menu111 in range(1,(calc_row_number("ElectricityTr") + 1)):
                        electricity_data = find_ElectricityTr(inp_menu111)
                        cost_charge100 = round(calc_ElectricityTr(car_data[6],electricity_data[3],electricity_data[4]),2)
                        cost_charge2080 = round(cost_charge100 * 0.6, 2)
                        clear()
                        print(menu_title())
                        print(f"\n {'Marka':{tbl_len_car}}: {car_data[1]}")
                        print(f" {'Model':{tbl_len_car}}: {car_data[2]}")
                        print(f" {'Motor':{tbl_len_car}}: {car_data[3]}")
                        print(f" {'Model yılı':{tbl_len_car}}: {car_data[4]}")
                        print(f"\n {'Batarya Kapasitesi':{tbl_len_car}}: {car_data[5]} kWh")
                        print(f" {'Kullanılabilir Kapasite':{tbl_len_car}}: {car_data[6]} kWh")
                        print(f"\n {'Elektrik Tarifesi':{tbl_len_car}}: {electricity_data[1]} - {electricity_data[2]}")
                        print(f"\n {'Tam Şarj Ücreti':{tbl_len_car}}: {cost_charge100} ₺")
                        print(f" {'%20-%80 Şarj Ücreti':{tbl_len_car}}: {cost_charge2080} ₺")
                        print(f"\n {'23°C Hava Sıcaklığında':{tbl_len_car}}  Menzil\t\tKm Maliyeti")
                        print(f" {'':-^{tbl_len_car}}  {'':-^{13}}  {'':-^{13}}")
                        print(f" {'Kullanıcı Menzili Şehiriçi':{tbl_len_car}}: {car_data[10]}km\t{round(cost_charge100/car_data[10],2)} ₺")
                        print(f" {'Kullanıcı Menzili Şehirdışı':{tbl_len_car}}: {car_data[11]}km\t{round(cost_charge100/car_data[11],2)} ₺")
                        print(f" {'Kullanıcı Menzili Karma':{tbl_len_car}}: {car_data[12]}km\t{round(cost_charge100/car_data[12],2)} ₺")
                        # print(f" {'Fabrika Menzili Şehiriçi':{tbl_len_car}}: {car_data[7]}km\t{round(cost_charge100/car_data[7],2)} ₺")
                        # print(f" {'Fabrika Menzili Şehirdışı':{tbl_len_car}}: {car_data[8]}km\t{round(cost_charge100/car_data[8],2)} ₺")
                        # print(f" {'Fabrika Menzili Karma':{tbl_len_car}}: {car_data[9]}km\t{round(cost_charge100/car_data[9],2)} ₺")
                        print(f"\n{'':-^{tbl_len_out}}")
                        if menu_bottom() == "break": break
                    else:
                        clear()
                        print(menu_title())
                        menu_error(inp_menu111)
                        print(f"\n{'':-^{tbl_len_out}}")
                        if menu_bottom() == "break": break
                except:
                    if inp_menu111.lower() == "q":
                        print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
                        break
                    elif inp_menu111.lower() == "a":
                        continue
                    else:
                        clear()
                        print(menu_title())
                        menu_error(inp_menu111)
                        print(f"\n{'':-^{tbl_len_out}}")
                        if menu_bottom() == "break": break

            else:
                clear()
                print(menu_title())
                menu_error(inp_menu11)
                print(f"\n{'':-^{tbl_len_out}}")
                if menu_bottom() == "break": break

        except:
            if inp_menu11.lower() == "q":
                print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
                break
            elif inp_menu11.lower() == "a":
                continue
            else:
                clear()
                print(menu_title())
                menu_error(inp_menu11)
                print(f"\n{'':-^{tbl_len_out}}")
                if menu_bottom() == "break": break

    # [12] Hibrit araç şarj/depo dolum maliyeti
    elif inp_mainmenu == "12":
        clear()
        print(menu_title())
        # print(f"\n Tüketim maliyetini hesaplamak istediğiniz aracın ID kodunu giriniz. ")
        # menu_car_hybrid()
        under_construction()
        print(f"\n{'':-^{tbl_len_out}}")
        # inp_menu11 = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        if menu_bottom() == "break": break

    # [13] Benzinli/Dizel araç depo dolum maliyeti hesapla
    elif inp_mainmenu == "13":
        clear()
        print(menu_title())
        print(f"\n Akaryakıt maliyetini hesaplamak istediğiniz aracın ID kodunu giriniz.\n")
        menu_car_fuel()
        print(f"\n{'':-^{tbl_len_out}}")
        inp_menu13 = input(f"\n [A] Ana menüye dön | [Q] Programdan Çık | Tercih: ")
        try:
            menu13 = int(inp_menu13)
            if menu13 in range(1,(calc_row_number("FuelCar") + 1)):
                car_data = find_fuel_car(inp_menu13)
                fuel_cost = calc_fuel_cost(car_data[7],car_data[8])
                clear()
                print(menu_title())
                print(f"\n {'Marka':{tbl_len_car}}: {car_data[1]}")
                print(f" {'Model':{tbl_len_car}}: {car_data[2]}")
                print(f" {'Motor':{tbl_len_car}}: {car_data[3]}")
                print(f" {'Model yılı':{tbl_len_car}}: {car_data[4]}")
                print(f"\n {'Motor hacmi':{tbl_len_car}}: {car_data[5]} cc")
                print(f" {'Motor gücü':{tbl_len_car}}: {car_data[6]} kWh")
                print(f" {'Yakıt Tipi':{tbl_len_car}}: {car_data[7]}")
                print(f" {'Akaryakıt depo hacmi':{tbl_len_car}}: {car_data[8]} lt")
                print(f"\n {'Tam Depo Dolum Ücreti':{tbl_len_car}}: {fuel_cost} ₺")
                print(f"\n {'23°C Hava Sıcaklığında':{tbl_len_car}}  Yakıt Tük.\tKm Maliyeti")
                print(f" {'':-^{tbl_len_car}}  {'':-^{13}}  {'':-^{13}}")
                print(f" {'Fabrika Menzili Şehiriçi':{tbl_len_car}}: {car_data[9]} l/100km\t{round(calc_fuel_cost_per_km(car_data[7],car_data[9]),2)} ₺")
                print(f" {'Fabrika Menzili Şehirdışı':{tbl_len_car}}: {car_data[10]} l/100km\t{round(calc_fuel_cost_per_km(car_data[7],car_data[10]),2)} ₺")
                print(f" {'Fabrika Menzili Karma':{tbl_len_car}}: {car_data[11]} l/100km\t{round(calc_fuel_cost_per_km(car_data[7],car_data[11]),2)} ₺")
                # print(f" {'Kullanıcı Menzili Şehiriçi':{tbl_len_car}}: {car_data[10]}km\t{round(cost_charge100/car_data[10],2)} ₺")
                # print(f" {'Kullanıcı Menzili Şehirdışı':{tbl_len_car}}: {car_data[11]}km\t{round(cost_charge100/car_data[11],2)} ₺")
                print(f" {'Kullanıcı Menzili Karma':{tbl_len_car}}: {car_data[14]} l/100km\t{round(calc_fuel_cost_per_km(car_data[7],car_data[14]),2)} ₺")
                print(f"\n{'':-^{tbl_len_out}}")
                if menu_bottom() == "break": break
        except:
            if inp_menu13.lower() == "q":
                print(f"\n{' İyi Günler ':=^{tbl_len_out}}\n")
                break
            elif inp_menu13.lower() == "a":
                continue
            else:
                clear()
                print(menu_title())
                menu_error(inp_menu13)
                print(f"\n{'':-^{tbl_len_out}}")
                if menu_bottom() == "break": break

        # if menu_bottom() == "break": break

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
            print(f"\n Görüntülemek istediğiniz araç markasını seçiniz.\n")
            print(menu_car_brands())
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
        print(f"\n Tüm araçlara ait bilgiler aşağıdadır.\n")
        show_all_cars()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [31] Güncel akaryakıt fiyatları
    elif inp_mainmenu == "31":
        clear()
        print(menu_title())
        print(f"\n Güncel akaryakıt fiyatları aşağıdadır.\n")
        show_current_FuelTr()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [32] Geçmiş akaryakıt fiyatları
    elif inp_mainmenu == "32":
        clear()
        print(menu_title())
        print(f"\n Geçmiş akaryakıt fiyatları aşağıdadır.\n")
        show_all_FuelTr()
        print(f"\n{'':-^{tbl_len_out}}")
        if menu_bottom() == "break": break

    # [41] Güncel elektrik fiyatları
    elif inp_mainmenu == "41":
        clear()
        print(menu_title())
        print(f"\n Güncel elektrik fiyatları aşağıdadır.\n")
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
