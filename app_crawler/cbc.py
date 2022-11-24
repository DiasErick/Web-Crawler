import requests
from bs4 import BeautifulSoup

def getCbcInfo(url: str, element: str):
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "lxml")
        elements = soup.select(element)
        return elements[0].text
    return ""

def getCbcInfoNews():
    return getCbcInfo("https://www.cbc.ca/news", '[class^="headline"]')
    
def getCbcInfoSports():
    return getCbcInfo("https://www.cbc.ca/sports", '[class^="headline"]')
    
def getCbcInfoRadio():
    return getCbcInfo("https://www.cbc.ca/radio", '[class^="headline"]')
    
def getCbcInfoMusic():
    return getCbcInfo("https://www.cbc.ca/music", '[class^="headline"]')
    
def getCbcInfoTelevision():
    return getCbcInfo("https://www.cbc.ca/television", '[class^="headline"]')