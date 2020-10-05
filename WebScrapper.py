import requests
from bs4 import BeautifulSoup
import pandas as pd;
url='https://www.matchesfashion.com/intl/mens/shop/shoes'


r=requests.get(url, headers = {'User-agent': 'Super Bot Power Level Over 9000','Accept-language':'da-DA'})
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
div=soup.find_all("div","lister__item__inner")
productPage=[]
imageLink=[]
brand=[]
name=[]
price=[]
for i in div:
    prev=" "
    link="https://www.matchesfashion.com/"
    for j in i.find_all('a',href=True):
        if j['href']!=prev:
            link=link+j['href']
            productPage.append(link)
        prev=j['href']
    for j in i.find_all('img'):
        imageLink.append('https:'+j['data-original']);
brandTag=soup.find_all('div','lister__item__title');
for i in brandTag:
    brand.append(i.getText())
nameTag=soup.find_all('div','lister__item__details');
for i in nameTag:
    name.append(i.getText())
priceTag=soup.find_all('span','lister__item__price-full');
for i in priceTag:
    price.append(i.getText())
print(price)    
dict={"Name":name,"Brand":brand,"Price":price,"Image Url":imageLink,"Product Url":productPage}
df=pd.DataFrame(dict)
df.to_csv('file1.csv');

       
        


