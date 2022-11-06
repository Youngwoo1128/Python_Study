"""
실습문제
정수들을 담은 nums 리스트가 있다.
num=[5, 15, 2, -8, -12, -29, 43, 1]

-29
"""
import random

nums=[5, 15, 2, -8, -12, -29, 43, 1]

min = nums[0]
for i in range(1, len(nums)):
    if min > nums[i]:
        min = nums[i]    
print(min)

print("=================================")

"""
num=[5, 15, 2, -8, -12, -29, 43, 1]
의 홀수 번째의 값들의 합을 구하시오
"""
sum = 0

for i in range(0, len(nums), 2):
   sum += nums[i]
print(sum)

print("=================================")

"""
로또번호 추출기를 만들어보자. (단, 번호가 중복되면 안된다.)
1 ~ 45 중 6개의 번호를 추출한다.
"""
lotto = []
for i in range (1, 46):
    lotto.append(i)

randomNumber = 0
prizes = []

for i in range(len(lotto)):
     randomNumber = random.randint(0, 45)
     if (randomNumber in lotto):
         if (len(prizes) == 6):
             break
         prizes.append(randomNumber)
         index = lotto.index(randomNumber)
         del lotto[index]

print(prizes)
     
print("=================================")

"""
선생님 풀이
"""

lotto_num = []
count = 0
while True:
    num = random.randint(1, 45)
    if num not in lotto_num:
        lotto_num.append(num)
        count += 1
        if count == 6: 
            break
print(lotto_num)