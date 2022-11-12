
"""
정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
"""

list = [1, 2, 3, 4, 5]
count = 0
result = 1

while count < 2:
    value = list[0]

    for i in range(len(list)):
        if value < list[i]:
            value = list[i]

    count += 1
    list.remove(list[list.index(value)])
    result *= value


print(result)  

list = [1, 5, 2, 6, 8]
value = list[-2] * list[-1]