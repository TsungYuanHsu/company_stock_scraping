import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'
r = requests.get(url)
print(f'Connection code is {r.status_code}')

soup = BeautifulSoup(r.text, 'html.parser')
print(f'The content of title attribute is {soup.title}')
print('The content from title tag is', soup.find_all('title'))
# print(soup.prettify())
table = soup.find('tbody')
# print(table.prettify())
rows = table.find_all('tr')
# print(rows)

stock_list = []
for row in rows:
    dict = {}
    columns = row.find_all('td')
    
    Date = columns[0].text
    Open = columns[1].text
    High = columns[2].text
    Low = columns[3].text
    Close = columns[4].text
    Adj_close = columns[5].text
    Volume = columns[6].text
    
    dict['Date'] = Date
    dict['Open'] = Open
    dict['high'] = High
    dict['low'] = Low
    dict['close'] = Close
    dict['adj_close'] = Adj_close
    dict['volume'] = Volume
    stock_list.append(dict)
# print(stock_list)

amazon_data = pd.DataFrame(stock_list)
print('The first 5 rows of stock data is \n', amazon_data.head())
print('\n')
print('The first 5 rows of stock data is \n', amazon_data.tail())
print(f'The names of columns is {amazon_data.columns}')