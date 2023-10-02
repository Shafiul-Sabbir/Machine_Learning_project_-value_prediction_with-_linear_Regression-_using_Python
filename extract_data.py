import requests
import re
import random
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf-8').decode('ascii','ignore')
soup = BeautifulSoup(text, 'lxml')
table = soup.find_all('table', class_='wikitable')[1]
rows = table.find_all('tr')[1:]

iphone_price_dict = {}
price = 200

for row in rows:
    data = row.find_all(['th','td'])
    try:
        version_text = data[0].a.text.split(' ')[1]
        version = re.sub(r"\D", "", version_text) 
        # re means regular expression, it converts char into texts
        version = int(version)
        price = price + 50
        if version and price > 100:
            # print(version, price)
            iphone_price_dict[version] = price
        
    except:
        pass

print(iphone_price_dict)

csv_fields = ['version', 'price']

with open('iphone_price.csv','w') as csvFile:
    csvwriter = csv.writer(csvFile)
    csvwriter.writerow(csv_fields)
    for key,value in iphone_price_dict.items():
        csvwriter.writerow([key,value])
    csvFile.close()
        