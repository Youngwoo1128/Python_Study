"""
파이썬에서는 숫자를 정수, 소수 두가지 표현 할 수 있다.
하지만 자바와는 다르게 딱 두가지의 자료형이 있다
int 와 float
"""
a = 5
b = -10
c = 120.0
d = 0.0
print(a, b, c, d, sep="\n")
print(a + b) # -5
print(c + b) #110.0
print(c - b) # 130.0
# 자료형은 달라도 역시 알아서 type casting 해줌
# 타입 확인하기
e = c + b
print(type(e))