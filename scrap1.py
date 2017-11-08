
import requests
from bs4 import BeautifulSoup
import pandas
pages=["http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/","http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=10.html"]
mls=list()
desc=list()
address=list()
price=list()
age=list()
img=list()
for p in pages:
    req=requests.get(p)
    content=req.content
    soup=BeautifulSoup(content,"html.parser")
    properties=soup.find_all("div",{"class":"propertyRow"})
    for propertyrow in properties:
        price.append(propertyrow.find_all("h4",{"class":"propPrice"})[0].text.strip())
        address.append(propertyrow.find_all("div",{"class":"primaryDetails"})[0].find_all("span",{"class":"propAddressCollapse"})[1].text.strip())
        desc.append(propertyrow.find_all("div",{"class":"propertyDescCollapse"})[0].text)
        mls.append(propertyrow.find_all("div",{"class":"propertyMLS"})[0].text[4:].strip())
        img.append(propertyrow.find_all("img",{"class":"lazyLoad"})[0]['rel'])
    
 
print(price,address,desc,mls,img)    
data=pandas.DataFrame({"prop_mls":mls,"prop_desc":desc,"prop_address":address,"prop_price":price,"prop_img":img})
print(data)