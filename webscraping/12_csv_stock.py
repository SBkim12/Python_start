import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf8", newline="") # 엑셀로 열때 한글파일 깨질시 - encoding="utf-8-sig"
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") # 탭으로 나눠진것을 리스트로 변환
print(type(title))
writer.writerow(title)


for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns] # 한줄 for 문
        # print(data)
        writer.writerow(data)