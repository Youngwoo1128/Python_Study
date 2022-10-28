"""
실습문제

1. 프로그램 사용자로부터 자연수n, m을 입력 받으면, n부터 m까지 합계를 계산해주는 프로그램을 작성해보자.
"""

# n = int(input())
# m = int(input())

# sum = 0
# for i in range(n, m + 1):
#     sum += i

# print(sum)


"""
다음 코드의 for 문을 while문으로 바꾸려고 합니다. 
빈칸에 들어 갈 내용을 채워 코드를 완성해보세요.

for i in range(1, 11, 2):
    print(i)
"""
i = 1

# while i <= 9:
#     print(i)
#     i += 2
#  틀림

# 정답
# while i < 11:
#     print(i)
#     i += 2



"""
3. 구구단 출력 프로그램을 만들어보자.
프로그램 사용자로 부터 출력할 단을 입력 받고, 해당 구구단을 출력하는 프로그램이다.

입력 몇 단을 출력할까요?:
"""

gugudanValue = int(input("입력 몇 단을 출력할까요?:"))

for i in range(1, 10, 1):
    # print(gugudanValue, "*", i , "=", gugudanValue * i)
    # 위에거 길어서 좀 불편함 그래서 이렇게 할 수 있음
    print(f'{gugudanValue} * {i} = {gugudanValue * i}')
    # 이렇게 쓰는걸 f-string 이라고 함