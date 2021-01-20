import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 처음으로 발견되는 a 태그 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 검색된 값중 처음으로 발견되는것 출력

# print(soup.find("li", attrs={"class" : "rank01"}))
rank1 = soup.find("li", attrs={"class" : "rank01"})
print("실시간 웹툰 1등 : ", rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# print("실시간 웹툰 2등 : ", rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print("실시간 웹툰 3등 : ", rank3.a.get_text())
# rank2_2 = rank3.previous_sibling.previous_sibling
# print(rank2_2.a.get_text())

# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print("실시간 웹툰 2등 : ", rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print("실시간 웹툰 3등 : ", rank3.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="고수")
print(webtoon)