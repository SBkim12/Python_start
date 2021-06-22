import re
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

for i in range(1, 6):

    print(" \n <{}페이지> \n".format(i))

    url = "https://papago.naver.net/website?locale=ko&source=en&target=ko&url=https%3A%2F%2Fwww.wolves.co.uk%2Fnews%2Ffirst-team%2F20210412-injury-update-on-neto-marcal-and-jonny%2F"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    print(soup)
