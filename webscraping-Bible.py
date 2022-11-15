import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


random_chapters = random.randint(1,21)

if random_chapters <10:
    random_chapters ='0' + str(random_chapters)
else:
    random_chapters=str(random_chapters)
'''
webpage = 'https://ebible.org/asv/JHN' +random_chapters +'.htm'

print(webpage)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage=urlopen(req).read()

soup=BeautifulSoup(webpage, 'html.parser')

page_verses=soup.findAll('div',class_="p")
for row in page_verses:
    verse_list = row.text.split('.')

myverse='Chapter:'+ random_chapters + ' Verse:'+ random.choice(verse_list[:len(verse_list)-2])
print(myverse)

'''
#spiit base on semicolomn with regit

random_chapters1 =str(random.randint(1,21))


webpage1 = 'https://biblehub.com/asv/john/' +random_chapters1 +'.htm'

print(webpage1)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage1, headers=headers)

webpage1=urlopen(req).read()

soup=BeautifulSoup(webpage1, 'html.parser')

page_verses=soup.findAll('div',class_="reg")
verse_list=[ ]
for row in page_verses:
    verse_list = row

print(verse_list)
#myverse='Chapter:'+ random_chapters + ' Verse:'+ random.choice(verse_list)
#print(myverse)