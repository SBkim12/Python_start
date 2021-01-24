import re
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

    #광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("<  광고 상품 제외  >")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    
    # 삼성 제품 제외
    if "삼성" in name:
        print(" < 삼성 제품 제외 > ")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()# 가격
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        print("  < 평점 없는 상품 제외 > ")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        print("  < 평점자 없는 상품 제외 > ")
        continue
    
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, "평점 : ", rate," 평점자 : ", rate_cnt)
    