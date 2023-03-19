from bs4 import BeautifulSoup
import requests

url= "https://www.pararius.com/apartments/amsterdam"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

for list in lists:
    title = lists.find('a' , class_="listing-search-iten__link--title")
    location = list.fin('div', class_="listing-search-item__location")
    price = list.find('span', class_="listing-search-item__price")
    area = list.find('a', class_="listing-search-item__link--title")
    info = [title, location, price, area]
    print(info)

