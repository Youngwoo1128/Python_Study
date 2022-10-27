"""
자료형 변환 : 데이터끼리 형식이 같다면 자료형을 변경할 수 있다.

1. 문자열 데이터 변환
: 정수 형태의 문자열은 정수로 변환 가능
: 실수 형태도 가능
: 숫자 데이터를 문자열로 변환도 가능
"""

# 정수
a = "100"
b = int(a)
c = int("200")
print(type(b), type(c))

# 그럼 이거는??
# d = int("qwe")
# 에러 -> ValueError: invalid literal for int() with base 10: 'qwe'

#이거는??
# d = int("!@#")
# 같은 에러

# 이것도 안됨
# d = int("100.5")
# invalid literal for int() with base 10: '100.5'