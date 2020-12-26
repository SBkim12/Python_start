from random import *

list1 = range(1,21) # 1부터 20까지의 숫자를 생성
print(type(list1)) # 타입이 range
list1 = list(list1) # 타입을 list로 변경
print(type(list1)) 
print(list1)

shuffle(list1)
print(list1)
print(sample(list1, 1))

winners = sample(list1, 4) # 4명중에서 1명은 치킨, 3명은 커피

print(" 당첨자 발표 ")
print("치킨당첨자 : {0}" .format(winners[0]))
print("커피당첨자 : {0}" .format(winners[1:]))
print(" 축하합니다 ")