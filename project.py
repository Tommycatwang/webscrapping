from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv
import keys2
from twilio.rest import Client
client=Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+13237011675"
myCellphone = '+12548787214'


url = 'https://coinmarketcap.com/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req= Request(url, headers=headers)
webpage=urlopen(req).read()

soup=BeautifulSoup(webpage, 'html.parser')

#title = soup.title

#print(title.text) search for text up and letter up


cell=soup.findAll('tr')

for x in cell[1:6]:
    cell2=x.findAll('td')
    cell3=x.findAll('span', class_='icon-Caret-down')
    cell4=x.findAll('p')
    if x:
        print(f"Name: {cell4[1].text}")
        print(f"Symbol:{cell4[2].text}")
        print(f"number: {cell2[3].text}")
        percent=float(cell2[5].text.replace("%",""))
        if cell3: 
            percent=percent*(1-2)
        print(f"24HR% change: {percent}%")
        number=float(cell2[3].text.replace(",","").replace("$",""))
        percent=float(number-(number*(percent/100)))
        print(f"the corresponding price is {round(percent,2)}")
        if cell2[2].text=="Bitcoin1BTC" and number <40000:
            print(f"Danger, the Bitcoin has get below the $40,000, becareful!")
            textmsg=client.messages.create(to=myCellphone, from_=TwilioNumber,body='the Bitcoin price in danger zone')

        if cell2[2].text=="Ethereum2ETH" and number<3000:
            print(f"Danger, the ethereum has get below the $3,000, becareful!")
            textmsg=client.messages.create(to=myCellphone, from_=TwilioNumber,body='the ethereum price is below 3000')

    print()
