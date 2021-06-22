import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument("headless")
# options.add_argument("--disable-gpu")
# options.add_argument("window-size=1920x1080")
options.add_argument(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

browser = webdriver.Chrome(options=options)

# 창이 완전히 열릴때까지 최대 4초 기다림
browser.implicitly_wait(4)

# 페이지 이동
url = "https://www.skysports.com/west-ham-united-news"
browser.get(url)

time.sleep(3)

soup = BeautifulSoup(browser.page_source, "lxml")

news_list = soup.select_one("#widgetLite-8 > div")

#news = news_list.find_all("div", attrs={"class":"news-list__item news-list__item--show-thumb-bp30"})
# for cartoon in cartoons:
#    rate = cartoon.find("strong").get_text()
#    print(rate)

for news in news_list.find_all('div', attrs={"class": "news-list__item news-list__item--show-thumb-bp30"}):
    a = news.a
    print("뉴스 주소:: " + a['href'])
    url = a['href']
    if url.endswith("transfer-centre") or url.find('/live/') != -1:
        continue

    try:
        browser.get(url)

        soup = BeautifulSoup(browser.page_source, "lxml")

        title = soup.find(
            "span", attrs={"class": "sdc-article-header__long-title"}).string
        print("기사제목 :: {0}".format(title))
        try:
            img = soup.find("img", {"class": "sdc-article-image__item"})
            src = img["src"]
            print("기사 이미지 :: {0}".format(src))
        except:
            src = null
            print("기사 이미지 없음 !")
        finally:
            print()
        contents = soup.find(
            "div", {"class": "sdc-article-body sdc-article-body--lead"})
        for content in contents.find_all(["p", "h3"]):
            print(content.get_text())
        # contents = soup.select(
        #    'body > div.section-wrap > div.sdc-site-layout-wrap.site-wrap.site-wrap-padding > div > div.sdc-site-layout__col.sdc-site-layout__col1 > div.sdc-article-body.sdc-article-body--lead > p')
        # for content in contents:
        #    print(content.text)
    except:
        print("-"*50)
        print("오류발생으로 인한 패스")
        continue
    finally:
        print("-"*200)

browser.quit()
