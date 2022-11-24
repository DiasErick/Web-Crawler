import requests
from bs4 import BeautifulSoup

def getCbcInfo(url: str, element: str):
    resp = requests.get("https://www.cbc.ca/" + url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "lxml")
        elements = soup.select(element)
        return elements[0].text
    return ""

def getCbcInfoNews():
    return getCbcInfo("news", '[class^="headline"]')
    
def getCbcInfoSports():
    return getCbcInfo("sports", '[class^="headline"]')
    
def getCbcInfoRadio():
    return getCbcInfo("radio", '[class^="headline"]')
    
def getCbcInfoMusic():
    return getCbcInfo("music", '[class^="headline"]')
    
def getCbcInfoTelevision():
    return getCbcInfo("television", '[class^="headline"]')