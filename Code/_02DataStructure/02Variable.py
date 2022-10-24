"""
변수

변수선언
cat_name = 고양이
"""

# cat_name = 고양이
# print(cat_name)
# error -> string은 "" 이나 ''으로,,,
from operator import truediv


cat_name = "고양이"
print(cat_name)

"""
그럼 이거는?
"""
var = "사슴"
var = "노루"
print(var)
# 노루 

"""
타입
"""

# boolean = true 
# 에러 -> 파이썬에서 boolean 은 첫글자를 대문자로...
boolean = True
boolean = False
print(boolean)

int = 1
print(int)

# long = 1L
# print(long)
# long은 따로 없나봄

float = 1.1
print(float)

character = 'a'
print(character) # 내 생각에 이건 String 같음

# 타입 확인하기
true = True
print(type(true))
# <class 'bool'>

"""
변수명 규칙
영문, 숫자, _ 만 가능
"""
한국 = "한국"
print(한국)
# 되는데..??

# 123 = 123
# print(123)
# 안됨 

# 그럼 이거는?
isTrue = 123 == 123
print(isTrue) #True
print(type(isTrue)) #<class 'bool'>

# 이것도 됨
stringValue = 한국 + "사람" 
print(stringValue) #한국사람
print("한국", "사람", "입니다.") #한국 사람 입니다.

#그럼 이거는??
# aaa = "a" + 1
# print(aaa)
# 에러