import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

#웹드라이버 로드
driver = webdriver.Chrome()
#지니챠트200 페이지에 접속 후 정보 얻어오기
url = 'https://music.bugs.co.kr/chart'
driver.get(url)

#얻어온 HTML소스를 파싱하기위해 Soup객체로 변환
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#파싱한 정보를 저장하기 위해 리스트 생성
song_data = []
rank = 1
#1~4페이지까지 순차적으로 반복

#챠트가 있는 Table에서 반복되는 요소 <tr>을 얻어옴
songs = soup.select('table.byChart > tbody > tr')
for song in songs:
    #제목
    title = song.select('p.title > a')[0].text
    #가수
    singer = song.select('p.artist > a')[0].text
    print(title,singer,sep="|")
    #제목과 가수, 순위까지 새로운 리스트를 생성 후 추가
    song_data.append(['Bugs',rank, title, singer])
    rank += 1

#크롤링이 완료되면 판다스를 이용해서 엑셀로 저장
columns = ['서비스','순위','타이틀', '가수']
#데이터프레임 생성 시 컬럼을 하나 추가
pd_data = pd.DataFrame(song_data, columns=columns)
#최상위 5개의 데이터 확인
print(pd_data.head())
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)