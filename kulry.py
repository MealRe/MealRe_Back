from tempfile import tempdir
from tokenize import String
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlopen
import csv
import pandas as pd
import pymysql

#db = pymysql.connect(host='172.31.35.173', port=3306, user='mealRe',
#password='Mealre2022!', db='oasis', charset='utf8')

#cur = db.cursor()

#sql = 'insert into oasisKor(indexNum, Name, DRate, DPrice, Oprice) values(%, %, %, %, %)'

# 한식: 795

url1 = f"https://www.oasis.co.kr/product/list?categoryId=795&page="
url2 = f"&sort=launchingDt&direction=desc&couponType=&rows=60"

url = f"https://www.kurly.com/shop/goods/goods_list.php?category=912003"

filename = 'oasis.csv'
f = open(filename, 'w', encoding='utf-8', newline='')
writer = csv.writer(f)

# table
oasis = requests.get(url1+"1"+url2)
soup = BeautifulSoup(oasis.content, "html.parser")
#table = soup.find('table', attrs={'class':'type_2'})

kulry = requests.get(url)
kulrySoup = BeautifulSoup(kulry.content, "html.parser")


"""# table row 가져오기
title_rows = table.find('thead').find_all('th')
titles = [title_row.get_text() for title_row in title_rows]

# print(titles)
writer.writerow(titles)"""

#print(url1 + '1' +url2)

pageCount = soup.select('.pagingWrap a span')
pageNum = 1
for i in pageCount:
    pageNum += 1
print(pageNum)

itemInfo = []
itemIndex = ["인덱스", "상품명", "할인율", "할인가", "원가", "이미지"]
itemInfo.append(itemIndex)

indexNum = 0

# rows 가져오기
for i in range (1, 5):
    #html = urlopen(url1 +str(i)+url2).read()
    html = urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')

    print(soup)

    total = soup.select('#goodsList .list_goods .item')
    #itemImage = soup.select('#goodsList .list_goods .name')
    itemName = soup.select('.name')
    #itemDRate = soup.select('.wrapInfo .info_price .price_discountRate')
    #itemDPrice = soup.select('.wrapInfo .info_price .price_discount b')
    #itemOPrice = soup.select('.wrapInfo .info_price .price_original b')
    #itemReview = soup.select('.info_group .info_reviewLike')

    num = 0
    #img = itemImage[0].get("src")

    print(itemName)

    for i in total:
        temp = []
        temp.append(indexNum)
        item = itemName[num].get_text()
        item = item.replace("\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
        item = item.replace('\n', "")
        item = item.replace('\t', "")
        temp.append(item)
        """item = itemDRate[num].get_text()
        item = item.replace("\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
        item = item.replace('\n', "")
        item = item.replace('\t', "")
        temp.append(item)
        item = itemDPrice[num].get_text()
        item = item.replace("\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
        item = item.replace('\n', "")
        item = item.replace('\t', "")
        temp.append(item)
        item = itemOPrice[num].get_text()
        item = item.replace("\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
        item = item.replace('\n', "")
        item = item.replace('\t', "")
        temp.append(item)
        item = itemImage[num].get("src")
        temp.append(item)"""
        """item = itemReview[num].get_text()
        item = item.replace("\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
        item = item.replace('\n', "")
        item = item.replace('\t', "")
        temp.append(item)"""
        num = num + 1
        indexNum = indexNum + 1

        itemInfo.append(temp)



"""for i in range(len(itemInfo)):
    dbData = []
    for j in range(len(itemInfo[i])):
        dbData.append(itemInfo[i][j])
    cur.execute(sql, tuple(dbData.values[i]))"""
        

for i in itemInfo:
     writer.writerow(i)
     #cur.execute(sql, itemInfo.values[i])

    #print(num)

f.close()

"""dbData = pd.read_csv("oasis.csv")
for i in range(len(dbData)):
    cur.execue(sql, tuple(dbData.values[i]))

#db.commit()
#db.close()
"""