
from bs4 import BeautifulSoup
import requests

url = 'https://weather.rambler.ru/v-moskve/today'
response = requests.get(url)
bs4 = BeautifulSoup(response.text, 'lxml')
temp = bs4.find('span', 'Njqa')
print(temp.text)


