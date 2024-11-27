from bs4 import BeautifulSoup
import requests, json

count = 0

chapterNum = int(input('Which chapter?'))
print(f'OK, Chapter {chapterNum} has been selected.')
response = requests.get(f'https://kanojo-okarishimasu.com/manga/rent-a-girlfriend-chapter-{chapterNum}/')
if response.status_code == 200:
    print('\nConnection Successful.\n')
elif response.status_code == 404:
    print('\n404: Page not found. I don\'t think you put in an existing manga chapter.')
else:
    print(response.status_code + 'Something went wrong...')
soup = BeautifulSoup(response.text, 'html.parser')
web = soup.prettify()
data_containers = soup.find_all('div', class_='img_container')
for i in range(0,len(data_containers)):
    images = data_containers[i].find('img')
    x = images.attrs['src']
    count += 1
    print(x)
print(f'\n{count} images located.')