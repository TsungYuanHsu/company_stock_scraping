import yfinance as yf
import pandas as pd
import requests

amd = yf.Ticker('NVDA')  # Create Ticker instance for AMD company

amd_json_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json'

r = requests.get(amd_json_url)
amd_json = r.json()
amd_country = amd_json['country']
amd_sector = amd_json['sector']

print(f'The country where AMD belongs to is {amd_country}')
print(f'The sector of AMD the stock belongs to is {amd_sector}')

amd_stock_max = amd.history(period='max')  # Get the historical stock data of AMD
amd_stock_max.reset_index(inplace=True)
print(amd_stock_max.head())

print(amd_stock_max.loc[0, 'Volume'])

amd_stock_max.plot(x='Date', y='Open')