python = "Python is Amazing"

print(python.lower()) #소문자 변환
print(python.upper()) #대문자 변환
print(python[0].isupper()) #대문자확인
print(len(python)) #길이확인
print(python.replace("Python", "Java")) # 글자 변환

index = python.index("n") # n이 위치한 위치
print(index)
index = python.index("n", index + 1) # n 이 위치한 다음 위치
print(index)

print(python.find("Java")) # Java가 포함된 위치 찾기(없으면 -1)
#print(python.index("Java")) # Java가 포함된 위치가 없으면 오류 출력

print(python.count("n")) # 문장에 포함된 n의 갯수