import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract_info():
    flat_type = []
    flat_area = []
    flat_price = []
    data = requests.get(
        'https://www.99acres.com/microsite/lutyens-realty-kalpataru-vista-sector-128-noida/?from_src=LI150095&src=FPLINK')
    soup = BeautifulSoup(data.text, 'html.parser')
    for i in soup.find_all('div', class_="divTableCell column-1"):
        flat_type.append(i.text)
    for j in soup.find_all('div', class_="divTableCell column-2"):
        flat_area.append(j.text)
    for k in soup.find_all('div', class_="divTableCell column-3"):
        flat_price.append(k.text)

    return flat_type, flat_area, flat_price


def csv_dump():
    ftype, farea, fprice = extract_info()
    df1 = pd.DataFrame(ftype, columns=['flat_type'])
    df2 = pd.DataFrame(farea, columns=['flat_area'])
    df3 = pd.DataFrame(fprice, columns=['flat_price'])

    df4 = pd.concat([df1, df2, df3], axis=1)
    df4.to_csv('..\\resource\\property.csv')


csv_dump()