filename = 'wingeat.csv'
f = open(filename, 'w', encoding='utf-8', newline='')
writer = csv.writer(f)

# table
wingeat = requests.get(url)
soup = BeautifulSoup(wingeat.content, "html.parser")
#table = soup.find('table', attrs={'class':'type_2'})


"""# table row 가져오기
title_rows = table.find('thead').find_all('th')
titles = [title_row.get_text() for title_row in title_rows]

# print(titles)
writer.writerow(titles)"""

#print(url1 + '1' +url2)

'''pageCount = soup.select('.pagingWrap a span')
pageNum = 1
for i in pageCount:
    pageNum += 1
#print(pageNum)'''

itemInfo = []
itemIndex = ["인덱스", "상품명", "할인율", "할인가", "원가"]
itemInfo.append(itemIndex)

indexNum = 0

# rows 가져오기
'''for page in range (1, pageNum):
   # print(i)
    html = urlopen(url).read()
    #print(url)

    soup = BeautifulSoup(html, 'html.parser')'''

total = soup.select('a, a:focus, a:hover')
print(len(total))
itemName = soup.select('.css-14wtbfn')
    #itemDRate = soup.select('.wrapInfo .info_price .price_discountRate')
    #itemDPrice = soup.select('.wrapInfo .info_price .price_discount b')
    #itemOPrice = soup.select('.wrapInfo .info_price .price_original b')
    #itemReview = soup.select('.info_group .info_reviewLike')

#print(itemName)
print(itemName[1])
ii = itemName[1].get_text()
print("이름: " + ii)
num = 0
print("이거: " + str(len(itemName)))
    
for i in range(len(total)):
        #print(total)
        temp = []
        temp.append(indexNum)
        item = total[i].get_text()
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
        temp.append(item)"""
        """item = itemReview[num].get_text()
        item = item.replace("\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t                \t", "")
        item = item.replace('\n', "")
        item = item.replace('\t', "")
        temp.append(item)"""
        num = num + 1
        indexNum = indexNum + 1

        itemInfo.append(temp)
    

for i in itemInfo:
     writer.writerow(i)

    #print(num)

f.close()

