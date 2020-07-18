import requests
from bs4 import BeautifulSoup
import os

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parer")
    pages = soup.find("div",{"class":"pagination"}).find_all("a")
    print(pages)

get_last_page()    
    
