from bs4 import BeautifulSoup
import requests
import pandas
base-url='http://www.mubawab.ma/fr/cr/grand-casablanca/'
#assetgroup={'immobilier-a-vendre-all':265,'immobilier-a-louer-all':345}
assetgroup={'immobilier-a-vendre-all':1}
pager=:p:
'''
transaction=['sale','rent']
asset=['apartments','commercial-property','farms','houses','land','riads','villas-and-luxury-homes']
asset-page-sale=[]
http://www.mubawab.ma/fr/cr/grand-casablanca/immobilier-a-vendre-all:p:2:sc:apartments-for-sale
http://www.mubawab.ma/fr/cc/immobilier-a-vendre-all:p:2
http://www.mubawab.ma/fr/cc/immobilier-a-vendre-all:p:2:sc:apartments-for-sale,commercial-property-for-sale,farms-for-sale,houses-for-sale,land-for-sale,riads-for-sale,villas-and-luxury-homes-for-sale
http://www.mubawab.ma/fr/cc/immobilier-a-louer-all:p:2
http://www.mubawab.ma/fr/cc/immobilier-a-louer-all:sc:apartments-for-rent,commercial-property-for-rent,farms-for-rent,houses-for-rent,land-for-rent,riads-for-rent,rooms-for-rent,villas-and-luxury-homes-for-rent
'''
for asset in assetgroup.keys():
    for page in range(1,assetgroup[asset])
    req=requests.get(base-url+asset+pager+page)
    cont=req.content
    price=list()
    aera=list()
    where=list()
    desc=list()
    soup=BeautifulSoup(cont,"html.parser")
    price.extend(soup.find_all('div',{'class':'nl-price'}).text.strip().replace('&nbsp',''))
    soup.find
print(price)




