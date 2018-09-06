import requests
from bs4 import BeautifulSoup
import csv
def extract_url():
    hotel_url=[]
    try:
        for i in range(1, 58):
            data = requests.get('https://www.wedmegood.com/vendors/all/wedding-venues/?page=' + str(i) + '')
            soup = BeautifulSoup(data.text, 'html.parser')
            for s in soup.find_all('a', {'class': ['vendor-detail text-bold h6']}):
                hotel_url.append('https://www.wedmegood.com' + s['href'])
        return hotel_url
    except Exception as e:
        print(e)

def some_info():
    url=extract_url()
    hotel_name=[]
    for all in url:
        data=requests.get(all)
        soup=BeautifulSoup(data.text,'html.parser')
        for name in soup.find_all(class_='Profile max-width-container margin-v-50 fcol'):
            hotel_name.append(name.find(class_='vendor-details h4 text-bold').get_text())
    print(hotel_name)
    print(len(hotel_name))
some_info()

