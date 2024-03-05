# 웹 크롤링 (Crawling) : 브라우저 드라이버를 이용하여 실제로 각 페이지를 이동하며 '동적'으로 데이터를 수집하는 방법
# 웹 스크래핑 (Scrapping) : 웹 페이지의 응답을 받아 데이터를 분석하여 필요한 데이터를 수집하는 방법 

# 파이썬 스크래핑 패키지 : Beautifulsoup4
# 파이썬 크롤링 패키지 : selenium

# pip install beautifulsoup4
# pip install selenium
# pip install requests

import requests
from bs4 import BeautifulSoup

URL = 'https://naver.com'
response = requests.get(URL)
print(response.status_code)

# 100 추가요청 기다림
# 200 성공
# 300 리소스위치 바뀜
# 400 요청자(클라이언트) 오류 
# 500 응답자(서버) 오류
# https://www.whatap.io/ko/blog/40/

# print(response.text)

if response.status_code == 200:
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  a_list = soup.find_all('a')
  print(a_list)

else:
  print(response.status_code)

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # 크롬실행

time.sleep(1) # 페이지가 완전히 로딩되고 시간되면 꺼짐

driver.get(URL) # 드라이버에 url 주소 넣고 실행
time.sleep(3)

search_input = driver.find_element(By.ID,'query')
search_input.send_keys('제네시스')
time.sleep(1)

search_input.send_keys(Keys.ENTER)
time.sleep(3)

news_button = driver.find_element(By.CSS_SELECTOR, '#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(8) > a')
time.sleep(1)

ActionChains(driver).click(news_button).perform()
time.sleep(3)







