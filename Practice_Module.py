# import Theater_module
# Theater_module.price(3) #3명이서 영화 보러감
# Theater_module.price_morning(4) #4명이서 조조 영화
# Theater_module.price_soldier(5) #5명의 군인 영화

# import Theater_module as mv #별명으로 이름 줄이기
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from Theater_module import *
# # from random import #
# price(3)
# price_morning(4)
# price_soldier(5)

# from Theater_module import price, price_morning #필요한것만 import
# price(5)
# price_morning(6)

from Theater_module import price_soldier as price #필요한것을 불러서 별칭사용
price(3)