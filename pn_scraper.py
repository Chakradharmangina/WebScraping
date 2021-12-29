import requests
from bs4 import BeautifulSoup
import pandas as pd
ai=0
furniturename=[]
links = []
furnituredetails = []
price = []
category = []
newsites = ['Sofa-Sets','Bean-Bag','Bed-Sets','Cabinets','Center-Tables','Conference-Tables','Dining-Chairs','Dining-Tables','TV-Units','Wardrobes','Center-Tables','Almirah','Dressing-Table','Recliners','Sofa-Cum-Bed','Garden Furniture','Shoe-Rack','Stool','Ottomans','Diwans','Inflatable-Bed','Massage-Bed']
#for i in newsites:
    #furniturename+=[i]*13
for ii in newsites:
    url = "https://www.quikr.com/home-lifestyle/"+ii+"+Home-Office-Furniture+Bangalore+w218fa"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    page = requests.get(url, headers=headers)
    content = BeautifulSoup(page.content, 'html.parser')
    data = content.find_all('div', {'itemtype': 'http://schema.org/Product'})
    for items in data:
        restlink = items.find('a')['href']
        name = items.find('h2', {'class': 'mdc-card__title'})
        furcatogire = items.find('li', {'class': 'brand-new'})
        furprice = items.find('p', {'class': 'mdl-typography--subhead'})
        furnituredetails.append(name.text)
        links.append(restlink)
        if furcatogire == None:
            category.append(" ")
        else:
            category.append(furcatogire.text.strip())
        price.append(furprice.text)
        furniturename.append(ii)
        ai+=1
    if ai>100:
        df = pd.DataFrame({'Furniture Type': furniturename, ' Furniture Details': furnituredetails, 'Price': price,'Category': category,'Link':links})
        df.to_csv('output.csv', index=False, encoding='utf-8')
        exit()