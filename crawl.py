import requests
from bs4 import BeautifulSoup


baseUrl = 'https://oto.com.vn/'
carLinks = []


for i in range(5):
    resp = requests.get(baseUrl + 'mua-ban-xe-cu-da-qua-su-dung/p' + str(i))
    suop = BeautifulSoup(resp.content,"html.parser")
    links = suop.select('.box-list-car .item-car > .photo > a')

    for link in links:
        carLinks.append(link['href'])

carLinks_str = ', '.join(carLinks)
print(carLinks_str)


file = open('car_links.txt', 'w')
for link in carLinks:
    file.write(link + '\n')