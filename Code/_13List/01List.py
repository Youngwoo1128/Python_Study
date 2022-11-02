"""
파이썬에서 리스트를 만드는 방법 

변수 = [데이터, 데이터, 데이터]

리스트 안 인덱스 별로 값 가져오는 방법
변수[0], 변수[1] ...

리스트에 값 할당 하는 법
list[0] = 값
list[1] = 값
list[2] = 값

리스트에 값 추가하는법

list.append(값)

데이터 삭제하는법
del list[0]

리스트 길이 리턴 받기 
len(list)

리스트 슬라이싱
list[start:end]
list[start:end:step]
"""

list = [1, 2, 3]
print(list[0])
print(list[1])
print(list[2])


list[0] = 5
list[1] = 7
print(list[0])
print(list[1])
print(list[2]) 

list.append(11)
list.append(13)
print(list)
# [5, 7, 3, 11, 13]

# del list[0]
# del list[1]
# print(list)
# [7, 11, 13]

del list[0]
del list[0]
print(list)
# [3, 11, 13]

# 오늘 파이썬의 [] 을 알기 전에는 배열인줄 알았는데 아님

size = len(list)
print(size)
# 3

# 리스트 슬라이싱
# list.append(100, 200)
# 한번에 두개 안됨 될줄 알았는데..
list.append(100)
list.append(200)
print(list[0 : 2])
# print(list[:2])

print(list)
print(list[0 : 3])

newList = []
newList.append("삼성전자")
newList.append("네이버")
newList.append("SK하이닉스")
newList.append("한국공항공사")
newList.append("한국도로공사")
print(newList[0:2])
# 예상 : ["삼성전자", "네이버", "SK하이닉스"]
# 답 : ['삼성전자', '네이버']
print(newList[0:3])
print(newList[0:10])
# 이렇게 해도 에러는 아님. 리스트 사이즈 보다 더 짤라도 끝까지 나옴

print(newList[1:3])
# ['네이버', 'SK하이닉스']

newList.append("대한항공")
newList.append("아시아나항공")
newList.append("제주항공")
newList.append("진에어")
newList.append("티웨이항공")
newList.append("이스타항공")
newList.append("에어부산")
newList.append("에어서울")
newList.append("에어로케이")
newList.append("플라이강원")
print(newList)
# ['삼성전자', '네이버', 'SK하이닉스', '한국공항공사', '한국도로공사', '대한항공', '아시아나항공', '제주항공', '진에어', '티웨이항공', '이스타항공', '에어부산', '에어서울', '에어로케이']
print(newList[::2])
# ['삼성전자', 'SK하이닉스', '한국도로공사', '아시아나항공', '진에어', '이스타항공', '에어서울']
print(newList[1: 7: 3])