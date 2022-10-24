""""
형변환
1. 파이썬 정수 변환 - int()
2. 파이썬 실수 변환 - float()
3. 파이썬 문자열 변환 - str()
4. 파이썬 문자 변환 - chr()
5. 파이썬 불리언 변환 - bool()
저기 파라미터에 넣으면 됨
"""
inputValue = input("값 입력 : ")
print(int(inputValue))
print(type(int(inputValue))) #<class 'int'>

print(bool(inputValue)) #True
print(type(bool(inputValue))) #<class 'bool'>
# ????? 이거 왜이럼 


print(chr(inputValue))
print(type(chr(inputValue)))
# 위에거 에러 string은 int 로 type casting 불가