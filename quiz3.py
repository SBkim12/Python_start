site = "http:\\naver.com"

main = site.replace("http:\\", "") # http:\\ 제거
main = main[:main.index(".")] # .이후 부분 제외

new_pwd = main[:3] + str(len(main)) + str(main.count("e")) + "!"
print(f"{site}의 비밀번호는 {new_pwd}입니다.")
