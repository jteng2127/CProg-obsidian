from bs4 import BeautifulSoup
import requests
import datetime

url_prefix = r'https://codeforces.com/gyms/page/'
url_postfix = r'?filterContestType=Official+ACM-ICPC+Contest&order=ID_DESC'

with open('all_contest_id.txt', 'w', encoding='utf-8') as f:
  f.write(str(datetime.datetime.now()) + '\n')
  page = 1
  while True:
    response = requests.get(url_prefix + str(page) + url_postfix)
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find("span", {"class": "page-index active"})['pageindex'] != str(page):
      break

    print(f'fetching page {page}')
    for id in soup.find_all("tr", {"data-contestid": True}):
      f.write(id['data-contestid'] + '\n')

    page += 1
