"""
다중 반복문 
그냥 똑같다.
"""

# for i in range(5):
#     for j in range(5):
#         print(i, j)


"""
실습문제

1. 다음 모양의 별을 출력해보자
*
**
***
****
*****
"""

# for i in range(6):
#     for j in range(0, i):
#         print("*", end = '')
#     print()


"""
*****
****
***
**
*
"""

for i in range(6, 0, -1):
    for j in range(1, i):
        print("*", end = '')
    print()

# 감소할때는 무조건 무조건 무조건 -1 감소 한다고 range 범위 꼭 적어줘야 함. 


"""
    *         4
   ***        3
  *****       2
 *******      1
*********     0
"""


# for i in range(1, 10, 2):
#     for j in range(0, i):
#         print("*", end="")
#     print()
# 실패

for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(2 * (i + 1) - 1):
        print("*", end="")
    print()