from lib2to3.pgen2 import driver
from tempfile import tempdir
from tokenize import String
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd
import pymysql

db = pymysql.connect(host='3.39.101.84', user='mealRe', password='', db='wingeat', charset='utf8')

cur = db.cursor()

sql0 = 'insert into diet values(%s, %s, %s)'
sql1 = 'insert into korSoup values(%s, %s, %s)'
sql2 = 'insert into fried values(%s, %s, %s)'
sql3 = 'insert into mealkit values(%s, %s, %s)'
sql4 = 'insert into riceNnoo values(%s, %s, %s)'
sql5 = 'insert into NM values(%s, %s, %s)'
sql6 = 'insert into street values(%s, %s, %s)'
sql7 = 'insert into riceC values(%s, %s, %s)'
sql8 = 'insert into bakery values(%s, %s, %s)'

sqlList = []

sqlList.append(sql0)
sqlList.append(sql1)
sqlList.append(sql2)
sqlList.append(sql3)
sqlList.append(sql4)
sqlList.append(sql5)
sqlList.append(sql6)
sqlList.append(sql7)
sqlList.append(sql8)

categoryList = [18, 8, 3, 2, 10, 17, 5, 7, 1]

"""
식단관리: 18
국/탕/찌개: 8
구이/볶음: 3
밀키트: 2
밥/면: 10
안주/야식: 17
분식/튀김: 5
떡/한과: 7
베이커리: 1
"""

url = f"https://www.wingeat.com/categories/"

filenameList = []
for i in range(len(categoryList)):
    filename = "wingeat" + str(i) + ".csv"
    filenameList.append(filename)

for k in range(0, len(categoryList)):
    f = open(filenameList[k], 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)

    wingeat = requests.get(url + str(categoryList[k]))
    soup = BeautifulSoup(wingeat.content, "html.parser")

    # print(url1 + str(categoryList[k]) + url2 + "1" + url3)

    """
    pageCount = soup.select('.pagingWrap a span')
    pageNum = 1
    for j in pageCount:
        pageNum += 1
    """

    itemInfo = []
    itemIndex = ["상품명", "가격", "이미지"]
    itemInfo.append(itemIndex)

    indexNum = 0

    # rows 가져오기
    html = urlopen(url + str(categoryList[k])).read()

    soup = BeautifulSoup(html, 'html.parser')

    total = soup.select(".css-14wtbfn")
    itemImage = soup.select('.css-jgo31c')
    itemName = soup.select(".css-14wtbfn")
    # itemDRate = soup.select('.css-1496eh5 ins')
    itemDPrice = soup.select('.css-1gm2phb')
    # itemOPrice = soup.select('.css-1h75cba del')
    # itemReview = soup.select('.info_group .info_reviewLike')

    #print(itemImage)


    num = 0

   # print(soup)

    for i in range(len(total)):
            temp = []
            #temp.append(num)
            item = itemName[num].get_text()
            temp.append(item)
            """item = itemDRate[num].get_text()
            item = item.replace(
                "\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
            item = item.replace('\n', "")
            item = item.replace('\t', "")
            temp.append(item)"""
            item = itemDPrice[num].get_text()
            temp.append(item)
            """item = itemOPrice[num].get_text()
            item = item.replace(
                "\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
            item = item.replace('\n', "")
            item = item.replace('\t', "")
            temp.append(item)"""
            item = itemImage[num].get("src")
            temp.append(item)
            """item = itemReview[num].get_text()
                item = item.replace(
                    "\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
                item = item.replace('\n', "")
                item = item.replace('\t', "")
                temp.append(item)"""
            num = num + 1

            itemInfo.append(temp)

    """for i in range(len(itemInfo)):
            dbData = []
            for j in range(len(itemInfo[i])):
                dbData.append(itemInfo[i][j])
            cur.execute(sql, tuple(dbData.values[i]))"""

    for i in itemInfo:
        writer.writerow(i)
        # cur.execute(sql, itemInfo.values[i])

        # print(num)

    f.close()



for i in range(len(categoryList)):
    dbData = pd.read_csv(filenameList[i])

    for j in range(1, len(dbData)):
        cur.execute(sqlList[i], tuple(dbData.values[j]))


db.commit()
db.close()
