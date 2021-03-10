from bs4 import BeautifulSoup
import csv
import requests
import time
import numpy as np
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)

# 페이지 이동
url = "https://lib.kopo.ac.kr/Customer/CustomerBookSearch.aspx?lib_code=P8759138&config_seq=8&menu_parentseq=8"
filename = "폴리도서목록.csv"
# 엑셀로 열때 한글파일 깨질시 - encoding="utf-8-sig"
f = open(filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)

title = "순번,도서명,저자,발행처,발행년".split(",")  # 탭으로 나눠진것을 리스트로 변환
print(type(title))
writer.writerow(title)

browser.get(url)

browser.find_element_by_id("ctl00_PlaceHolderCustomer_ctl00_btnSearch").click()
time.sleep(4)  # 4초간 대기

page = 1
while page <= 793:

    soup = BeautifulSoup(browser.page_source, "lxml")

    for list_no in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']:
        data_row = soup.find("table").find("tbody").find("tr", attrs={
            "id": "ctl00_PlaceHolderCustomer_ctl00_rptSearchList_ctl{}_trLink".format(list_no)})

        columns = data_row.find_all("td")

        data = [column.get_text().strip() for column in columns]
        del data[5:]

        print(data)

        writer.writerow(data)

    if page == 1:
        browser.find_element_by_xpath(
            "//*[@id=\"ctl00_PlaceHolderCustomer_ctl00_lblPageList\"]/a[1]").click()
        time.sleep(2)
    elif page == 10:
        browser.find_element_by_xpath(
            "//*[@id=\"ctl00_PlaceHolderCustomer_ctl00_lblPageList\"]/a[11]").click()
        time.sleep(2)
    elif page % 10 == 0:
        browser.find_element_by_xpath(
            "//*[@id=\"ctl00_PlaceHolderCustomer_ctl00_lblPageList\"]/a[12]").click()
        time.sleep(2)
    elif page < 10:
        browser.find_element_by_xpath(
            "//*[@id=\"ctl00_PlaceHolderCustomer_ctl00_lblPageList\"]/a[{}]".format(page+1)).click()
        time.sleep(2)
    else:
        browser.find_element_by_xpath(
            "//*[@id=\"ctl00_PlaceHolderCustomer_ctl00_lblPageList\"]/a[{}]".format(page % 10+2)).click()
        time.sleep(2)

    page = page+1
