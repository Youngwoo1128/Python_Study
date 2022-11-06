inputValue = int(input())

answer = 0
temp = inputValue
n = 0

while True:
    n = temp // 10
    answer += temp % 10
    temp = n
    if temp == 0: break



print(answer)