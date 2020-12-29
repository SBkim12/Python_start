gun = 10

def checkpoint(soldiers): #경계근무
    global gun # 전역 공간에 있는 gun 사용 , 권장 하지 않는 방법
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}". format(gun))

def checkpoint_ret(gun, soldiers): #전역변수를 끌고 와 사용하는 것을 권장
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun



print("전체 총 : {0}".format(gun))
checkpoint_ret(gun, 2) # 경계근무 2명 출격
#checkpoint(2) # 경계근무 2명 출격
print("남은 총 : {0}".format(gun))