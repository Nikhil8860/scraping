import requests
from bs4 import BeautifulSoup
def all_url():
    url=[]
    name=[]
    link=requests.get('http://upworktestru.com/python-test-upwork-answers-questions/')
    soup=BeautifulSoup(link)
    print(soup)

all_url()
