"""
사용자에게 값을 입력 받고
역삼각형으로 만들기

입력
5

출력
*****
 ****
  ***
   **
    *

"""

inputValue = int(input())

for i in range(inputValue):
    for j in range(inputValue - i, 0, -1):
        print("*", end="")
        if (j == 1): print()
    for j in range(i + 1):
        print(" ", end="")
    