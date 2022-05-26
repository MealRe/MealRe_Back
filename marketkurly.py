import requests
from bs4 import BeautifulSoup as bs

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
}
crawlUrl = 'https://api.kurly.com/v1/categories/029?page_limit=99&page_no=1&delivery_type=0&sort_type=1&ver=1653555963649'
crawl = requests.post(crawlUrl, data={'': '', '': ''}, headers=header)
'''import json

response = requests.get(
    'https://api.kurly.com/v1/categories/029?page_limit=99&page_no=1&delivery_type=0&sort_type=1&ver=1653555963649').text
jsonObject = json.loads(response)['data']

for i in range(99):
    print(jsonObject['products'][i]['name'])
    print(jsonObject['products'][i]['discount_percent'])
    print(jsonObject['products'][i]['discounted_price'])
    print(jsonObject['products'][i]['original_price'])'''


"""#import pymysql
import requests

request_headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjYXJ0X2lkIjoiZGIzNDRiMDktNTgwNy00YjUyLWIyZWItMmI0YzQwZTc3MDk2IiwiaXNfZ3Vlc3QiOnRydWUsInV1aWQiOm51bGwsIm1fbm8iOm51bGwsIm1faWQiOm51bGwsImxldmVsIjpudWxsLCJzdWIiOm51bGwsImlzcyI6Imh0dHA6Ly9ta3dlYi5hcGkua3VybHkuc2VydmljZXMvdjMvYXV0aC9ndWVzdCIsImlhdCI6MTY1MzUwMjMxOSwiZXhwIjoxNjUzNTA1OTE5LCJuYmYiOjE2NTM1MDIzMTksImp0aSI6ImNncVhvTlp2ZlNnVHlCV2IifQ.CvkpHq2_v8IGWr5jRcou_nSelZ3aY5GksIQVCsidCT4'
}

url = "https://www.kurly.com/shop/goods/goods_list.php?category=912"

response = requests.get(url, headers=request_headers)
data = response.json()
items = data['data']['items']

result = []

result = [{
    'no': item['no'],
    'name': item['name'],
    'price': item['price']
} for item in items]

for value in result:
    print(value)
print(data)"""

"""conn = pymysql.connect(host='172.31.35.173', port=3306,
                       user='mealRe', password='Mealre2022!', charset='utf8', db='marketkurly')
cur = conn.cursor()

sql = "CREATE TABLE market(indexNum, Name, Oprice);"
cur.execute(sql)  # sql수행

# id AUTO_INCREMENT COMMENT PRIMARY KEY

sql = "INSERT INTO market(indexNum, Name, Oprice) VALUES (%,%,%);"
# values = ( ? , ? , ? )
cur.execute(sql, values)

#sql = "ALTER TABLE 테이블이름 DROP COLUMN 컬럼이름"

#sql = "DELETE FROM market;"

#sql = "DROP TABLE market;"

result = cur.fetchall()
print(result)

conn.commit()
conn.close()"""
