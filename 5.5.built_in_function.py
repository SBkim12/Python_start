# abs 절대값을 반환
print('---abs---')
print(abs(-3))

# all 반복 가능한 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴 함
print('---all---')
print(all([1, 'false', 2, 3, 4]))
print(all([1, 'false', 2, 3, 4, 0]))  # 0은 false

# any x중 하나라도 참이 있을 경우 True를 리턴하고 x가 모두 거짓일 경우에만 False를 리턴 함
# all의 반대
print('---any---')
print(any([1, 'false', 2, 3, 4]))
print(any([1, 'false', 2, 3, 4, 0]))  # 0은 false

# chr 아스키 코드를 입력 받아 그 코드에 해당하는 문자 반환
print('---chr---')
print(chr(97))

# ord 문자의 아스키 코드 값 리턴 chr과 반대
print("---ord---")
print(ord("a"))

# divmod(a, b) a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴하는 함수임 [몫, 나머지]
print('---divmod---')
print(divmod(7, 3))

# enumerate 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴 함
print('{0:-^17}'.format("enumerate_1"))  # 총 17자리 enumerate 중앙에 두고 남는 공간 - 로 채움
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print("---enumerate_2---")  # 총 15자리 enumerate 중앙에 두고 남는 공간 - 로 채움
for name in enumerate(['body', 'foo', 'bar']):
    print(name)

# eval 실행 가능한 문자열을 입력으로 받아 실행한 결과값을 리턴하는 함수
print('---eval_1---')
print(eval('1+2'))

print('---eval_2---')
print(eval('"ho"+"w"'))  # ""씌워줘야 계산 가능

print('---eval_3---')
print(eval('divmod(4, 3)'))

# filter(함수, 반복 가능한 자료형) 반복가능한 자료형 요소들이 함수에 입력됬을 때 참인 거만 묶어서 반환
print('---filter---')


def positive(x):
    return x > 0


print(list(filter(positive, [1, -3, 2, 3, -5, -2, 6, 0])))  # list로 묶지 않으면 <filter object at 0x000001B4FC2383C8>가 반환됨

# hex 정수값을 받아 16진수로 변환
print('---hex---')
print(hex(16))

# id 객체를 입력받아 객체의 고유한 주소값을 반환(C 에서는 포인터 주소)
print('---id---')
a = 3
print(id(3))
print(id(a))

# input 사용자의 입력을 받음 (java 에서는 scanner c 에서는 scanf )
print('---input---')
a = input()
print(a)
b = input("값을 입력하세여 : ")
print(b)

# int 문자열 형태의 숫자 or 실수를 정수 형태로 반환
print('---int_1---')
print(int('3'))
print(int(4.2))
# int(a, b) b의 진수로 표현된 수 'a'를 10진수로 반환
print('---int_2---')
print(int('11', 2))  # '11'은 2진수로 표현한 수
print(int('2A', 16))

# isinstance(a, class) a가 class의 인스턴스 인지 확인
print("---isinstance---")


class Person: pass


a = Person()
b = 3
print(isinstance(a, Person))
print(isinstance(b, Person))

# lambda 함수 생성 예약어 def와 동일 함수를 한줄로 간결하게 만들떄 사용
print("---lambda_1---")
sum_1 = lambda a, b: a + b  # sum_2와 동일
print(sum_1(1, 3))


def sum_2(a, b):  # sum_1과 동일
    return a + b


print("---lambda_2---")
myList = [lambda a, b: a + b, lambda a, b: a * b]
print(myList[0](3, 4))
print(myList[1](3, 4))

# len 입력값 s의 길이(요소의 전체 개수)
print("---len---")
print(len('abcdef'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 'b')))

# list 반복가능한 자료 s를 받아 리스트로 반환
print("---list---")
print(list("123124123"))

# map(함수, 반복가능 자료형) 반복가능한 자료형의 요소가 함수 수행결과를 묶어 반환
print("---map---")


def two_times_1(x): return x * 2


two_times_2 = lambda a: a * 2

print(map(two_times_1, [1, 2, 3, 4]))
print(list(map(two_times_2, [1, 2, 3, 4])))

# max 반복가능한 자료형을 받아 최대값을 반환
print("---max---")
print(max([1, 2, 3, 4, 5]))

# min 반복가능한 자료형을 박아 최소값을 반환
print("---min---")
print(min([1, 2, 3, 4, 5]))

# open(파일명, 읽기 방법) w: 쓰기 r: 읽기 a: 추가 b: 바이너리
# default r
print("---open---")
f = open("foo.txt", "r")

# pow(a, b) a에 b제
print("---pow---")
print(pow(2, 4))  # 2의 4제곱
print(2 ** 4)

# range(a, b, c) a부터 b까지. a가 없으면 0부터 시작. c는 숫자 사이의 거리. 끝숫자는 포함X
print("---range---")
print(list(range(5)))
print(list(range(1, 5)))

# sorted 입력값을 정렬수 리스트로 반환
print("---sorted---")
print(sorted([8, 1, 6, 2, 5, 3, 7, 4]))

# str 문자열형태로 변환후 반환
print("---str---")
print(str(3))

# tuple tuple형태로 변환후 반환
print("---tuple---")
print(tuple(list("12345")))

# type 입력값의 자료형 반환
print("---type---")
print(type("3"))
print(type(3))

# zip 동일한 개수로 이루어진 자료형을 묶어줌. 튜플은 그대로 리턴
print("---zip---")
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))

# shutil.copy(src, dst) src라는 이름의 파일을 dst로 복사함