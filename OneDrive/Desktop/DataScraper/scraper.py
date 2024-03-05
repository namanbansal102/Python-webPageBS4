import requests
import random as rad
from bs4 import BeautifulSoup
url="https://www.westside.com/collections/man-jackets-waistcoats"
r_url="http://localhost:3000/api/addpro"
r=requests.get(url)
lst=[]

soup=BeautifulSoup(r.text,"lxml")
prices=soup.find_all("span",class_="boost-pfs-filter-product-item-regular-price")
images=soup.find_all("img",class_="boost-pfs-filter-product-item-main-image")
categories=soup.find_all("p",class_="boost-pfs-filter-product-item-vendor")
titles=soup.find_all("a",class_="boost-pfs-filter-product-item-title")
print((images[0])['data-src'])
for title,category,image,price in zip(titles,categories,images,prices):
    realP=((price.text).split(" ")[1])
    realP=realP.split(",")
    realP="".join(realP)
    myobj={
        "title":title.text,
        "slug":title.text,
        "desc":"It is a very Good Western Dress For Women For PartyWear use",
        "img":image['data-src'],
        "category":category.text,
        "price":int(float(realP)),
        "size":"men_XL_Jackets",
        "color":"Not mentioned",
        "quantity":rad.randrange(1,50)
    }
    # print(myobj)
    
    x=requests.post(r_url,json=myobj)
    print(x.content)
    

