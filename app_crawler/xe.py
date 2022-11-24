from bs4 import BeautifulSoup
import requests

class XeCrawler(object):
    def __init__(self):
        #Crawl XE results for exchanging
        
        super().__init__()
        
        #Adding a header
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Host': 'www.xe.com',
            'Referer': 'https://www.xe.com/'
        }

    def __get_source(self, url: str) -> requests.Response:
        
        #Get the web page's source code        
        return requests.get(url, headers=self.headers)

    def search(self, amount: str,currency_from: str, currency_to: str):
        #Search the currency exchanging information
        
        # Get response from XE web site, sengind the amount, origin currency and the desired currency
        response = self.__get_source('https://www.xe.com/currencyconverter/convert/?Amount= '+ amount + '&From=' + currency_from + '&To=' + currency_to)
        
        #Just checking if the result was successful
        if response.status_code == 200:
            
            # Initialize BeautifulSoup
            soup = BeautifulSoup(response.text, "lxml")
            
            #Getting the class with result
            elements = soup.select('[class^="result__BigRate-sc-1bsijpp-1 iGrAod"]')
            return elements[0].text
                
        return ""