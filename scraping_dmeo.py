import requests
from bs4 import BeautifulSoup
import csv

"""def extract_data_web():
    try:
        product_name=[]
        product_url=[]

        data=requests.get('https://www.olx.in/cars/')
        soup=BeautifulSoup(data.text,'html.parser')
        for a in soup.find_all('a', class_='marginright5 link linkWithHash detailsLink',href=True):
            product_name.append(a['href'])
            p=[i.strip() for i in product_name]

            product_url.append(a.text)
        return p,product_url

        for b in soup.find_all('strong', class_='c000'):
            product_price.append(b.text)
        #print(product_price)
        r=[x.strip()for x in product_price]
        return r
    except Exception as e:
        raise e"""

"""def write_data_csv():
    product_name,product_url=extract_data_web()
    print(product_name)
    print(product_url)
    with open('..\\resource\\olx_user_name.csv','w',newline='') as csv_file:
        data=csv.writer(csv_file)
        data.writerow(['product_name'])
        for row in product_name:
            data.writerow([row])
        print("Write data suucess")

    '''df=pd.DataFrame(product_name ,columns=['Names'])
    df1=pd.DataFrame(product_url,columns=['Url'])
    combine=pd.concat([df,df1])
    print(combine)'''
write_data_csv()"""



def extract_data():
    hotel_name=[]
    hotel_url=[]
    hotel_address=[]
    for i in range(1,58):
        data=requests.get('https://www.wedmegood.com/vendors/all/wedding-venues/?page='+str(i)+'')
        soup=BeautifulSoup(data.text,'html.parser')
        for s in soup.find_all('a', {'class': ['vendor-detail text-bold h6']}):
            hotel_name.append(s.text)
            hotel_url.append('https://www.wedmegood.com'+s['href'])
        for a in soup.find_all('p',class_='vendor-detail'):
            hotel_address.append(a.text)

    return hotel_name,hotel_address,hotel_url



def all_data():
    hotel_name=[]
    hotel_addr=[]
    hotel_phone=[]
    hotel_about=[]
    hotel_rating=[]

    name, address, url = extract_data()
    for all in url:
        data = requests.get(all)
        soup = BeautifulSoup(data.text, 'html.parser')
        for n in soup.find_all('h1', {'class': ['vendor-details h4 text-bold']}):
            hotel_name.append(n.text)

        for a in soup.find_all('p', {'class': ['text-tertiary']}):
            hotel_addr.append(a.text)

        for p in soup.find_all('h6', {'class': ['h6 green']}):
            hotel_phone.append(p.text)

        for rating in soup.find_all('span', {'class': ['StarRating center rating-4 h4 large']}):
            hotel_rating.append(rating.text)

        for descr in soup.find_all('div', {'class': ['info padding-h-20 padding-v-20']}):
            hotel_about.append(descr.text)

    return hotel_name,hotel_addr,hotel_phone,hotel_rating,hotel_about

def csv_dump():
    hotel_name, hotel_addr, hotel_phone, hotel_rating, hotel_about=all_data()
    with open('..\\resource\\all_data.csv','w',newline="") as f:
        w=csv.writer(f)
        w.writerow(['Hotel_name','Hotel_address',' hotel_phone','hotel_rating','hotel_about'])
        for i,j,k,l,m in zip(hotel_name,hotel_addr,hotel_phone,hotel_rating,hotel_about):
            w.writerow([i,j,k,l,m])
        print("Write success")

import pandas as pd
try:
    df=pd.read_csv('..\\resource\\employee_file.csv')
    print(df)
except FileNotFoundError as e:
    print(e)
#testing 2