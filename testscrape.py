from bs4 import BeautifulSoup
import requests

response = requests.get('https://komisanwamanga.com/')
if response.status_code == 200:
   print('It worked!')
soup = BeautifulSoup(response.text, 'html.parser')
web = soup.prettify()
data_containers = soup.find_all('div', class_='entry-content')
images = data_containers[0].find('a')
print('\n\n\n\n\n'+str(images))