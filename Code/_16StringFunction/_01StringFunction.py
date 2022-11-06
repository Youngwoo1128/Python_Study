"""
파이썬의 String 함수들
"""

# 문자열 갯수
message = "탑 이기고 있으니까 기다려 탑캐리 가자"
print(message.count("탑"))

# 문자 찾기
name = "startcoding"
print(name.find("t"))

# 문자열 바꾸기
sayHello = "hello, hello, hello, hello, what's up"
sayHi = sayHello.replace("hello", "hi")
print(sayHi)

# 문자 자르기
text = "파이썬 아따 쉽구마잉~!"
print(text.split())
# 얘는 리스트로 리턴하는것 같음
fruits = "orange,bananna,pineapple"
print(fruits.split(","))


# 문자 합치기
text = ["Monday", "Friday", "Saturday"]
print(''.join(text)) # MondayFridaySaturday
print(' '.join(text)) # Monday Friday Saturday
print(":".join(text)) # Monday:Friday:Saturday

"""
공백문자 제거
"""
text = "                   아따 날씨 좋구마이!           "
print(text.strip())
print(text.rstrip())
print(text.lstrip())