from urllib.request import urlopen
from bs4 import BeautifulSoup


njsbcl = 'https://www.njsbcl.com/'


try :
  html_doc = urlopen(njsbcl)
  soup = BeautifulSoup(html_doc, 'html.parser')

except: 
  print('error bitch')



try :
  sponsor = [s.get_text(strip=True) for s in soup.find_all("h4")]

  top_players_batting =  soup.find("div", class_="players")
  


except: 
  print('cant find all')

print(top_players_batting)

# for sponsor in sponsor : 
#   print(sponsor)
  
