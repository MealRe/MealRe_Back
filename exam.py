import csv
import urllib.request
from urllib.parse import quote_plus
from urllib.request import urlopen
from bs4 import BeautifulSoup

### 검색 및 데이터 받아오기
search = input('검색어를 입력해주세요. : ')

# quote_plus = 한글 인코딩 역할
url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={quote_plus(search)}'
html = urlopen(url).read()

# 해당 주소에 있는 모든 내용을 soup 변수에 담음
soup = BeautifulSoup(html, 'html.parser')

# 개발자 도구 찍어서 원하는 부분 선택 (아래 예시는 네이버 view 부분)
total = soup.select('.api_txt_lines.total_tit')
searchList = []

# find_all = 전부 가져오겠다 / find: 하나의 결과값만 가져오겠다
# class는 이미 파이썬에서 사용하고 있는 예약어이기 때문에 언더바를 같이 써야 함

# attrs = 속성
# 마찬가지로 가져오고 싶은 속성명은 개발자 도구로 확인해보기
for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)
	# searchList를 프린트해서 데이터가 잘 받아와졌는지 확인


### csv 파일 저장
# 저장된 파일을 메모장에서 열어서 ANSI로 다시 저장 후 엑셀에서 열면 한글 안 깨짐
# newline = 한 줄 내리기
    f = open(f'{search}.csv', 'w', encoding='utf-8', newline='')    
    csvWriter = csv.writer(f)

    for i in searchList:
        csvWriter.writerow(i)
    f.close()