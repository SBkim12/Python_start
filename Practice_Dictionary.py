cabinet = {3:"유재석", 100:"김태호"} # 키값 설정
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) #키값이 없을 경우 오류 발생 및 중지
print(cabinet.get(5)) #키값이 없을 경우 None 표시
print(cabinet.get(5, "사용 가능")) #키 값이 없을 경우 ,뒤 값 표시

print(3 in cabinet) #값이 있으면 True
print(5 in cabinet) #값이 없으면 False

cabinet = {"A-3":"유재석", "B-100" :"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

# Key, Value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
