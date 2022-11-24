import requests
from bs4 import BeautifulSoup

class CbcCrawler(object):
    def __init__(self):
        
        super().__init__()
        
        #Adding a header
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Host': 'www.cbc.ca',
            'Referer': 'https://www.cbc.ca/'
        }
    
    def __get_source(self, url: str) -> requests.Response:
        #Get the web page's source code 
        return requests.get(url, headers=self.headers)
    
    def search(self, option: str) -> str:
        
        url_base = "https://www.cbc.ca/"
        url = url_base
        option = option.lower()
        
        #Cheking the optons value to define the url
        match option:
            case "sports": url  += option
            case "news": url += option
            case "radio": url += option
            case "tv": url += option
            case "music": url += option
        
        #If we processed an valid option, we can go ahead and check the web site
        if url != url_base:
            response = self.__get_source(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "lxml")                
                elements = soup.select('[class^="headline"]') #taking the content we want
                return elements[0].text
            
        return ""