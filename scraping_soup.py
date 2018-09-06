import requests
from bs4 import BeautifulSoup
import urllib

'''def learn_soup():
    source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
    soup = BeautifulSoup(source, 'html.parser')
    nav=soup.nav
    body=soup.body
    table=soup.table
    table=soup.find('table')
    table_row=table.find_all('tr')
    for body in body.find_all('p'):
        print(body.text)
    for url in nav.find_all('a',href=True):
        print(url['href'])
    for tr in table_row:
        td = tr.find_all('td')
        row = [i.text for i in td]
        print(row)
learn_soup()'''


def extract_data_web():
    l=[]
    try:
        data=requests.get('https://www.99acres.com/microsite/lutyens-realty-kalpataru-vista-sector-128-noida/?from_src=LI150095&src=FPLINK')
    except Exception as e:
        print(e)
    else:
        soup=BeautifulSoup(data.text,'html.parser')
        for i in soup.find_all('div',class_='divTable'):
            l.append(i.text)
        x=[i.strip() for i in l]

extract_data_web()


