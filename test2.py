# Fuel Price Watcher Script

import datetime
import requests
# from bs4 import BeautifulSoup as soup
from bs4 import BeautifulSoup

today = str(datetime.date.today())
post_url = "https://www.turkiyeshell.com/pompatest/"
company = "Shell Türkiye"

data = {"city": "ANKARA",
"district": "ANKARA_ÇANKAYA"}

response = requests.post(post_url, data=data)
print(response.status_code)
# print()
# soup=BeautifulSoup(response.content,"html.parser")
# print(soup)

# print(today,company,fuel_price)