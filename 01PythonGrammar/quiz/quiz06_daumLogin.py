'''
퀴즈] 
https://www.daum.net/ 접속 후 카카오계정으로 로그인 버튼 클릭
==> 아이디,비번 입력 후 로그인 버튼 클릭 ==> 메인으로 이동
==> 검색어 입력 후 검색결과 페이지 확인 
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://www.daum.net/'
driver.get(url)

driver.find_element(By.XPATH,'//*[@id="loginMy"]/div/div[1]/div/a').click()
time.sleep(2)

driver.find_element(By.NAME, 'loginId').send_keys('aiueoeom@naver.com')
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys('zlxlvoa97!')

driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[1]/form/div[4]/button[1]').click()
time.sleep(30)

driver.find_element(By.XPATH, '//*[@id="q"]').click()
time.sleep(2)

driver.find_element(By.NAME, 'q').send_keys('뉴스')
time.sleep(2)

driver.find_element(By.CLASS_NAME,'btn_ksearch').click()
time.sleep(10)

