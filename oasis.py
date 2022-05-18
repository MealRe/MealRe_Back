import requests
from bs4 import BeautifulSoup

oasis = requests.get("https://www.oasis.co.kr/product/list?categoryId=120&page=1&sort=&direction=&couponType=&rows=60")
soup = BeautifulSoup(oasis.content, "html.parser")

for x in range (0, 10):
    print("상품명: ", soup.select('.listTit')[x].get_text())
    print("할인율: ", soup.select('.price_discountRate')[x].get_text())
    print("할인가: ", soup.select('.price_discount')[x].get_text())
    print("원가: ", soup.select('.price_original')[x].get_text(), '\n\n')
