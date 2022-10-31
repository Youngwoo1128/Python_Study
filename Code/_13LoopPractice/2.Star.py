"""
사용자에게 정수를 입력 받고 그 정수 만큼의 * 피라미드 만들기

예 ->

입력 
3

출력

   *
  ***
 *****

"""

inputValue = int(input())

for i in range(inputValue):
    for j in range(inputValue - i, 0, -1):
        print(" ", end="")
    for j in range(2 * (i + 1) - 1):
        print("*", end="")
    print()
    
