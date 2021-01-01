print("Python", "Java","JavaScript", sep=" vs ", end="?") 
print("무엇이 더 재밌을까요?")
# sep은 ,로 나뉘어진 부분의 값을 정해줌
# end는 원래는 줄바꿈인데 다른 것으로 마지막을 변경할수 있음

import sys
print("Python", "java", file=sys.stdout) #표준출력
print("Python", "java", file=sys.stderr) #표준에러로 출력

#시험성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): #.items() - key와 value를 출력
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    #.ljust(8) - 8칸의 공간을 확보하고 좌측 정렬
    #.rjust(4) - 4칸의 공간을 확보하고 우측 정렬


#은행 대기순번표
# 001, 002, 003, ....
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
    #.zfill(3) - 3칸의 공간을 확보하고 나머지 빈공간은 0으로 채우기

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) #input으로 들어가는 값은 str값으로 저장된다
print("입력하신 값은 " + str(answer) + "입니다.")