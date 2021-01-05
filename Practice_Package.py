# import travel.thailand #패키지 임포트
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to =  thailand.ThailandPackage()
trip_to.detail()

#import하는 파일의 위치 파악
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))