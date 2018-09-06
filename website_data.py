import requests
from bs4 import BeautifulSoup
def all_url():
    url=[]
    name=[]
    link=requests.get('http://upworktestru.com/python-test-upwork-answers-questions/')
    soup=BeautifulSoup(link.text,'html.parser')


all_url()
