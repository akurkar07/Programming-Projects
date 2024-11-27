from bs4 import BeautifulSoup
import requests

count = 0

response = requests.get('https://komisanwamanga.com/manga/komi-can-t-communicate-vol-12-chapter-159-the-fourth-great-you-better-not-be-loud-test-study-session/')
print('Visited URL: {}'.format(response.url))
if response.status_code == 200:
   print('Connection Successful.')
soup = BeautifulSoup(response.text, 'html.parser')
web = soup.prettify()
data_containers = soup.find_all('div', class_='separator')
for i in range(0,len(data_containers)):
   images = data_containers[i].find('img')
   x = images.attrs['src']
   count += 1
   print(x)
print(str(count) + ' images located.')
