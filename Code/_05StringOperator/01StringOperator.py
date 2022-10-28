"""
문자열을 숫자만큼 이어줌 
이게 무슨 말이냐
"""
string = "startCoding" * 2
print(string)

string = "startCoding" * 0
print(string)
# 이야 이거 안나오네
print("woo" * 3)

# 그럼 이거는??
# string = "startCoding" * 1.1
# print(string)
# 에러 ㅋㅋㅋ
# TypeError: can't multiply sequence by non-int of type 'float'
# 나누기도 안됨 ㅋㅋ