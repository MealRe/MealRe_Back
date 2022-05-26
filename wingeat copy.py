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

driver = webdriver.Safari()
driver.get('https://www.wingeat.com/categories/2')
driver.execute_script("window.scrollTo(0, 900)")

html = driver.page_source
soup = BeautifulSoup(html)

#itemList = driver.find_element("p", {"class":"css-14wtbfn"})
#print(len(itemList))

#url = f"https://www.wingeat.com/categories/2"

prev_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 화면 가장 아래로 내린다
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(2)

    # 현재 문서 높이를 가져와서 저장
    curr_height = driver.execute_script("return document.body.scrollHeight")

    if(curr_height == prev_height):
        break
    else:
        prev_height = driver.execute_script("return document.body.scrollHeight")

#itemList = curr_height.select('.css-14wtbfn')
print(curr_height)

