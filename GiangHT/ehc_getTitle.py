import requests
from bs4 import BeautifulSoup
 
url = "https://dantri.com.vn/the-thao.htm"
 

r = requests.get(url)
 
soup = BeautifulSoup(r.content, 'html.parser')
 
print("============TITLE=============")

print(soup.title.text)

temp = soup.select_one('div.row')

temp2 = temp.select('h3.article-title')

for i in temp2:
    print(i.text)

t = soup.select_one('div.row.line.mt-30')
t2 = t.select_one('div.col.col-840')
t3 = t2.select('h3.article-title')

for z in t3:
    print(z.text)
