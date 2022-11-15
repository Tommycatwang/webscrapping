from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

url = 'https://registrar.web.baylor.edu/exams-grading/fall-2022-final-exam-schedule'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req= Request(url, headers=headers)
webpage=urlopen(req).read()

soup=BeautifulSoup(webpage, 'html.parser')

