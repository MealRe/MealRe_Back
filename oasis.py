from tempfile import tempdir
from tokenize import String
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlopen
import csv
import pandas as pd
import pymysql

db = pymysql.connect(host='3.39.101.84', port=22, user='mealRe',
password='', db='oasis', charset='utf8')

cur = db.cursor()

sql = 'insert into easyMeal(indexNum, Name, DRate, DPrice, Oprice, itemImg) values(%, %, %, %, %, %)'

"""
가정간편식
    간편식사: 57
    아침식사대용: 60
    베스트야식: 87
    엄마표 간식: 91
    국/탕/찌개: 33
    죽/스프/카레: 54

간식/유제품
    떡/빵/한과/엿: 248
    시리얼: 249

농산
    채소/샐러드: 137
"""

categoryList = [57, 60, 87, 91, 33, 54, 248, 249, 137]

url1 = f"https://www.oasis.co.kr/product/list?categoryId="
url2 = f"&page="
url3 = f"&sort=priority&direction=desc&couponType=&rows=60"

filenameList = []
for i in range(len(categoryList)):
    filename = "oasis" + str(i) + ".csv"
    filenameList.append(filename)

# table

for k in range(0, len(categoryList)):
    f = open(filenameList[k], 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)

    oasis = requests.get(url1 + str(categoryList[k]) + url2 + "1" + url3)
    soup = BeautifulSoup(oasis.content, "html.parser")

    #print(url1 + str(categoryList[k]) + url2 + "1" + url3)

    pageCount = soup.select('.pagingWrap a span')
    pageNum = 1
    for j in pageCount:
        pageNum += 1

    itemInfo = []
    itemIndex = ["인덱스", "상품명", "할인율", "할인가", "원가", "이미지"]
    itemInfo.append(itemIndex)

    indexNum = 0

    # rows 가져오기
    for page in range (1, pageNum):
        html = urlopen(url1 + str(categoryList[k]) + url2 + str(page) + url3).read()

        soup = BeautifulSoup(html, 'html.parser')

        total = soup.select('.wrapInfo')
        itemImage = soup.select('.oPrdtLst .wrapImg img')
        itemName = soup.select('.wrapInfo .info_title .innerBox .inner a')
        itemDRate = soup.select('.wrapInfo .info_price .price_discountRate')
        itemDPrice = soup.select('.wrapInfo .info_price .price_discount b')
        itemOPrice = soup.select('.wrapInfo .info_price .price_original b')
        #itemReview = soup.select('.info_group .info_reviewLike')

        num = 0

        #print(soup)

        
        for i in total:
            temp = []
            temp.append(indexNum)
            item = itemName[num].get_text()
            item = item.replace("\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
            item = item.replace('\n', "")
            item = item.replace('\t', "")
            temp.append(item)
            item = itemDRate[num].get_text()
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
            temp.append(item)
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

dbData = pd.read_csv("oasis0.csv")

print(dbData)

for i in range(len(dbData)):
    cur.execute(sql, tuple(dbData.values[i]))

db.commit()
db.close()