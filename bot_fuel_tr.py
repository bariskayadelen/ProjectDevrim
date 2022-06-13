# Web sayfasından otomatik akaryakıt fiyatlarını alan script

import urllib.request
from bs4 import BeautifulSoup as soup

url = "https://www.aytemiz.com.tr/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
uClient = urllib.request.urlopen(req)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html.decode('utf-8','ignore').encode("utf-8"), 'html5lib')
fuel_price = page_soup.find_all('div', {"class":"fuel-price"})[0].text.strip().strip('TL/LT')
diesel_price = page_soup.find_all('div', {"class":"fuel-price"})[1].text.strip().strip('TL/LT')
lpg_price = page_soup.find_all('div', {"class":"fuel-price"})[3].text.strip().strip('TL/LT')

print(f"\nBenzin Fiyatı: {fuel_price}  |  Dizel Fiyatı: {diesel_price}  |  LPG Fiyatı: {lpg_price}\n")

bdm = float(fuel_price) * 54
print(f"Bir depo dolum maliyeti: {bdm} TL'dir.\n")