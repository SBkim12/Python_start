from random import *

cnt = 0 #총 탑승 승객 수

for customer_no in range(1,51):
    time = randrange(5, 51) # 5분 ~ 50분 소요시간
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분".format(customer_no, time))
        cnt+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(customer_no,time))

print("총 탑승 승객 : {0} 분" .format(cnt))