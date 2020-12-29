def profile(name, age, *language): # *변수명은 넣고싶은만큼 값들을 넣을수 있다.
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")  #end를 사용하면 줄바꿈 하지 않고 end값 생성후 다음 것 출력
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")