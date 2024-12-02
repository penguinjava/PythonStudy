from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#드라이버 로드
driver = webdriver.Chrome()

#네이버 메인에 접속
url = 'https://www.naver.com/'
driver.get(url)

#XPath를 이용해서 네이버 메인의 로그인 버튼을 클릭
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
#로드와 상관없이 무조건 2초 대기
time.sleep(2)

#로그인 페이지로 이동 후 아이디/비번의 입력상자(input)를 찾은 후
#본인의 정보 입력
driver.find_element(By.NAME, 'id').send_keys('ironi123')
time.sleep(2)
driver.find_element(By.NAME, 'pw').send_keys('')
time.sleep(2)


#입력 후 로그인 버튼을 클릭해서 로그인 시도
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()
time.sleep(30)
#셀레니움 로그인을 감지하므로 캡챠 화면이 뜬다.
#조금 김 시간을 대기하면서 직접 입력한다.

#로그인이 완료되면 메인으로 자동 이동하므로 상단의 검색창에 검색어를 입력
driver.find_element(By.NAME, 'query').send_keys('셀레니움')
time.sleep(2)

#검색 버튼을 눌러서 결과를 확인
driver.find_element(By.CLASS_NAME, 'byn_search').click()
time.sleep(10)