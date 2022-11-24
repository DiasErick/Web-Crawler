import requests
from bs4 import BeautifulSoup

def getCbcInfoNews():
    URL = "https://www.cbc.ca/news"
    resp = requests.get(URL)
    if resp.status_code == 200:     
        soup = BeautifulSoup(resp.text, "lxml")        
        elements = soup.select('[class^="headline"]')
        return elements[0].text
    
def getCbcInfoSports():
    URL = "https://www.cbc.ca/sports"
    resp = requests.get(URL)
    if resp.status_code == 200:     
        soup = BeautifulSoup(resp.text, "lxml")        
        elements = soup.select('[class^="headline"]')
        return elements[0].text
    
def getCbcInfoRadio():
    URL = "https://www.cbc.ca/radio"
    resp = requests.get(URL)
    if resp.status_code == 200:     
        soup = BeautifulSoup(resp.text, "lxml")        
        elements = soup.select('[class^="headline"]')
        return elements[0].text    
    
def getCbcInfoMusic():
    URL = "https://www.cbc.ca/music"
    resp = requests.get(URL)
    if resp.status_code == 200:     
        soup = BeautifulSoup(resp.text, "lxml")        
        elements = soup.select('[class^="headline"]')
        return elements[0].text
    
def getCbcInfoTelevision():
    URL = "https://www.cbc.ca/television"
    resp = requests.get(URL)
    if resp.status_code == 200:     
        soup = BeautifulSoup(resp.text, "lxml")        
        elements = soup.select('[class^="headline"]')
        return elements[0].text
    
def getCbcInfo():
    headline_cbc_news = getCbcInfoNews()
    headline_cbc_sports = getCbcInfoSports()
    headline_cbc_radio = getCbcInfoRadio()
    headline_cbc_music = getCbcInfoMusic()
    headline_cbc_tv = getCbcInfoTelevision()
    
    return [headline_cbc_news, headline_cbc_sports, headline_cbc_radio, headline_cbc_music, headline_cbc_tv]