import requests

# request로 사이트 여는게 막혀 있는 경우
# url = "http://nadocoding.tistory.com"
# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"} # whatismybrowser.com를 통해서 무엇을 통해 사이트를 여는지 확인 가능

# res = requests.get(url, headers=headers)
# res.raise_for_status()

res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)