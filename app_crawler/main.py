from nasdaq import NasdaqCrawler
from cbc import CbcCrawler

#################################################################
#Here I'm testing a web crawler to get headline from CBC web site
#################################################################
obj_cbc = CbcCrawler()
option = "News" #Available options: Sports, News, Radio, Tv, Music
result_cbc = obj_cbc.search(option)

#Cheing if we got the result
if result_cbc:
  print("\nHere is Headline from CBC for " + option + ":\n'" + result_cbc +"'\n" )
else:
  print("\nWe could't get Headline for " + option + ", lets try again?\n")

###########################################################################################
#Here I'm testing a web crawler to get some values about currency exchanging in EX web site.
###########################################################################################

#Setting the amount and both currencies
amount = "250.10" ; curr_ori = 'BRL' ; curr_to = "CAD"

obj_nasdaq = NasdaqCrawler()
result = obj_nasdaq.search(amount, curr_ori, curr_to)
#Printing the result
if result:  
  print("\nHere is your result of exchanging: \n" + amount + " " + curr_ori +" = " + result.split()[0] + " " + curr_to + "\n")  
else:
  print("We could't get your result from exchanging informations, lets try again?")