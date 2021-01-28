from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동

#가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("29")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("30")[0].click() # [0] -> 이번달

# 다음달 27일, 28일 선택
browser.find_elements_by_link_text("30")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("27")[1].click() # [0] -> 이번달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 브라우저를 최대 10초 까지 기다리며 지정된 위치가 있으면 동작 실행
try:
    elem = WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을때 동작 수행
    print(elem[0].text) # 첫번째 결과 출력
finally:
    print("동작 시간 초과")
    browser.quit()
# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")