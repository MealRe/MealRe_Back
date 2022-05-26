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

categoryList = [18, 8, 3]

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
    itemImage1 = soup.select('.css-jgo31c')
    itemImage2 = soup.select('.css-1qzwu6t')
    itemImage3 = soup.select('.css-1qzwu6t')
    #itemName = soup.select(".css-14wtbfn")
    # itemDRate = soup.select('.css-1496eh5 ins')
    #itemDPrice = soup.select('.css-1gm2phb')
    # itemOPrice = soup.select('.css-1h75cba del')
    # itemReview = soup.select('.info_group .info_reviewLike')

    print(itemImage1[0])
    print("-=====")
    print(len(itemImage1))
    #print(itemImage2)
    #print(itemImage3)


    num = 0

   # print(soup)

    for i in range(1):
            temp = []
            temp.append(num)

            item = itemImage1[num].get("src")
            print("1:")
            print(item)
            temp.append(item)

            """item = itemReview[num].get_text()
                item = item.replace(
                    "\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
                item = item.replace('\n', "")
                item = item.replace('\t', "")
                temp.append(item)"""
            num = num + 1

            itemInfo.append(temp)

    for i in itemInfo:
        writer.writerow(i)
        # cur.execute(sql, itemInfo.values[i])

        # print(num)

f.close()