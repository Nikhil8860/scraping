import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
'''page=requests.get('https://pythonprogramming.net/robotics-raspberry-pi-tutorial-gopigo-introduction/')
soup=BeautifulSoup(page.text,'html.parser')
print(soup.p.text)
print(soup.text)
print(soup.get_text)
for url in soup.find_all('a'):
    print(url.get('href'))'''

'''page=requests.get('https://pythonprogramming.net/robotics-raspberry-pi-tutorial-gopigo-introduction/')
soup=BeautifulSoup(page.text,'html.parser')'''
'''for url in soup.find_all('a'):
    print(url.get('href'))'''

'''for url in soup.find_all('a',href=True):
    print(url['href'])'''
'''soup=soup.nav
for url in soup.find_all('a'):
    print(url.get('href'))'''


'''body=soup.body
for para in body.find_all('p'):
    print(para.text)'''

'''page=requests.get('https://pythonprogramming.net/parsememcparseface/')
soup=BeautifulSoup(page.text,'html.parser')
#table=soup.table
table=soup.find('table')
table_rows=table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)'''

#pandas version to read table

'''dfs=pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)
for df in dfs:
    print(df)'''


#xml file read
'''page=requests.get('https://pythonprogramming.net/sitemap.xml')
soup=BeautifulSoup(page.text,'xml')
for url in soup.find_all('loc'):
    print(url.text)'''


'''page=requests.get('https://pythonprogramming.net/parsememcparseface/')
soup=BeautifulSoup(page.text,'html.parser')
js_test=soup.find('p',class_='jstest')
print(js_test.text)'''

'''page=requests.get('https://accessibility.umn.edu/web-designers/tables-web-pages')
soup=BeautifulSoup(page.text,'html.parser')
for data in soup.find_all('table'):
    for table_row in data.find_all('tr'):
        print(table_row.text)'''

'''dfs=pd.read_html('https://accessibility.umn.edu/web-designers/tables-web-pages',header=0)
for df in dfs:
    print(df)'''

# flipkart new launch mobile
"""u=[]
x=[]
p=[]
import webbrowser
def get_url(url):
    try:
        data=requests.get(url)
    except Exception as e:
        print(e)
    else:
        soup=BeautifulSoup(data.text,'html.parser')
        for i in soup.find_all('a',class_='K6IBc- required-tracking'):
            u.append('https://www.flipkart.com'+i.get('href'))
        for j in range(len(u)-10):
            webbrowser.open(u[j])

get_url('https://www.flipkart.com/')"""

'''info=[]
data=requests.get('https://mindmajix.com/python-interview-questions')
soup=BeautifulSoup(data.text,'html.parser')
table=soup.find('table')
table_rows=table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)'''

'''dfs=pd.read_html('https://mindmajix.com/python-interview-questions',header=0)
for df in dfs:
    print(df)'''

'''data = requests.get('http://examples.yourdictionary.com/examples-of-antonyms-synonyms-and-homonyms.html')
soup=BeautifulSoup(data.text,'html.parser')
table=soup.find('table')
table_row=table.find_all('tr')
for tr in table_row:
    td=tr.find_all('td')
    x=[i.text for i in td]
    print(x)'''

data = requests.get('http://examples.yourdictionary.com/examples-of-antonyms-synonyms-and-homonyms.html')
soup=BeautifulSoup(data.text,'html.parser')
encode=soup.encode('utf-8')
print(encode)
