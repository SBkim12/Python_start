from selenium import webdriver
import time


browser = webdriver.Chrome() # 폴더 위치에 맞춰서, 같은 폴더 위치에 있으면 위치정보 필요 없음 - "./chromedriver.exe"

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")


# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(2) # 3초간 대기

# 5. id를 새로 입력
#brwoser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
browser.quit() # 정베 브라우저 종료