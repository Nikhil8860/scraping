from time import sleep
from random import randint
import csv,requests
from bs4 import BeautifulSoup
urls=[]
f = csv.writer(open('..\\resource\\jdphone.csv', 'w', newline=''))
f.writerow(['Name', 'Price'])
for i in range(1,5):
	urls.append('https://www.justdial.com/Shop-Online/Mobile-Phone/nid-11216691/page-'+str(i))
for url in urls:
	sleep(randint(1,3))
	siteData=requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
	#print(siteData.text)
	data=BeautifulSoup(siteData.text,'html.parser')
	for dt in data.findAll(class_='shopboxinner'):
		#print(dt)
		names=dt.find(class_='disp_height').text
		price=dt.find(class_='dt_price').text
		f.writerow([names, price])
print("write data success")
