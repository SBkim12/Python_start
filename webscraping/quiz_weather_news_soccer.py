import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8"
    # soup = create_soup(url)

    now = soup.find("p", attrs={"class","info_temperature"}).get_text().replace("도씨", "")
    detail = soup.find("p", attrs={"class","cast_txt"}).get_text()
    low = soup.find("span", attrs={"class","min"}).get_text()
    high = soup.find("span", attrs={"class","max"}).get_text()

    # 강수 확률
    rain_morning = soup.find("span", attrs={"class","point_time morning"}).get_text().strip()
    rain_after = soup.find("span", attrs={"class","point_time afternoon"}).get_text().strip()

    #미세먼저
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text() #미세먼지
    pm25 = dust.find_all("dd")[1].get_text() #초미세먼지

    print(detail)
    print(f"현재 : {now}  (최저 {low} / 최고 {high})")
    print(f"오전 강수확률 {rain_morning} / 오후 강수확률 {rain_after}\n")
    print(f"미세먼지 {pm10} \n초미세먼지 {pm25}")

def scrape_headline():
    print("[오늘 뉴스 헤드라인]")
    url = "https://news.naver.com"
    soup = create_soup(url)

    headlines = soup.find("ul", attrs={"class","hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(headlines):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("(링크 : {})".format(link))

if __name__ == "__main__":
    # scrape_weather() #오늘 날씨 정보 가져오기
    scrape_headline() #오늘의 뉴스 헤드라인 가져오기

