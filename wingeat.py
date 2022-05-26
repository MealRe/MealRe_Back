from lib2to3.pgen2 import driver
from tempfile import tempdir
from tokenize import String
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen
import csv
import time

"""
db = pymysql.connect(host='3.39.101.84', port=22, user='mealRe',
password='', db='oasis', charset='utf8')

cur = db.cursor()

sql = 'insert into easyMeal(indexNum, Name, DRate, DPrice, Oprice, itemImg) values(%, %, %, %, %, %)'

"""

categoryList = [18, 8, 3, 2, 10, 17, 5, 7, 1]

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
    itemIndex = ["인덱스", "상품명", "가격", "이미지"]
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
            temp.append(num)
            item = itemName[num].get_text()
            item = item.replace(
                "\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
            item = item.replace('\n', "")
            item = item.replace('\t', "")
            temp.append(item)
            """item = itemDRate[num].get_text()
            item = item.replace(
                "\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
            item = item.replace('\n', "")
            item = item.replace('\t', "")
            temp.append(item)"""
            item = itemDPrice[num].get_text()
            item = item.replace(
                "\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
            item = item.replace('\n', "")
            item = item.replace('\t', "")
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

# dbData = pd.read_csv("oasis0.csv")


# for i in range(len(dbData)):
#    cur.execute(sql, tuple(dbData.values[i]))

# db.commit()
# db.close()
