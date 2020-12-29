def profile(name, age=17, main_lang="파이썬"): #기본값 설정하는 부분
    print("이름 : {0}\t 나이 : {1} \t 주사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")
profile("김승범")