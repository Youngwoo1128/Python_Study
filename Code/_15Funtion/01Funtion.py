"""
파이썬에서 함수 생성하는 법

def 함수이름(인자값):
    명령블럭
    return 반환값
"""

def add_num(a, b):
    res = a + b
    return res

result = add_num(10, 20)
print(result)

"""
결과 값이 없는 함수
"""
def div_num(a, b):
    res = a / b
    print(res)
div_num(10, 20)

"""
매개변수가 없는 함수
"""

import random
def get_random_number():
    n = random.randint(1, 100)
    return n
print(get_random_number())

"""
결과값, 매개변수가 없는 함수
"""
def say_hello():
    print("안녕하세요!")
    print("반갑습니다!")

say_hello()