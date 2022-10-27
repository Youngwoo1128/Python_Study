"""
실습문제 
1. 프로그램 사용자로부터 자연수 n을 입력 받으면, 1부터 n까지 합계를 계산해주는 프로그램을 작성해보자.
"""

inputValue = int(input())

sum = 0

for i in range(inputValue):
    sum += i + 1
print(sum)