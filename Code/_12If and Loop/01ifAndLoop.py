"""
조건문과 반복문의 결합
"""

# while True:
#     order = input("명령 내려주세요:")
#     if order == "go":
#         print("계속합니다.")
#     elif order == "stop":
#         print("종료합니다.")
#         break
#     else:
#         print("잘못 입력했습니다.")


"""
실습문제
1. 
숫자 1입력 : "게임을 시작합니다" 출력
숫자 2입력 : "실시간 랭킹" 출력
숫자 3입력 : "게임을 종료합니다" 출력
단, 3을 입력 할때 까지 프로그램은 계속 실행된다. 1~3이 입력되면 "다시 입력해 주세요." 출력
"""

isLoop = True
while isLoop:
    print("[메뉴를 입력하세요]")
    print("1. 게임시작", "2. 랭킹보기", "3. 게임종료", ">>>", end = "")
    inputValue = int(input())
    if inputValue == 1:
        print("-> 게임을 시작합니다.")
    elif inputValue == 2:
        print("-> 실시간 랭킹")
    elif inputValue == 3:
        print("게임을 종료합니다.")
        isLoop = False
    else:
        print("다시 입력해 주세요.")
