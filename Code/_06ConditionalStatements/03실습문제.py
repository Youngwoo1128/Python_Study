"""
실습문제

1. 회사를 그만두게 된 유진이는 유튜브를 시작하게 되었다
그리고, 유튜브를 통해 수익창출을 하려고 한다.
프로그램 사용자로부터 현재 구독자 수를 입력 받으면, 수익 창출이 가능한지 불가능한지
알려주는 프로그램을 작성해보자. (단, 수익창출은 구독자가 1000명 이상일 경우 가능하다.)

가능하면: "수익 창출이 가능합니다!"
불가능하면: "수익 창출이 불가능합니다!"
"""

# minAvailable = 1000
# inputValue = int(input("현재 구독자 수를 입력해 주세요: "))

# if minAvailable <= inputValue:
#     print("수익 창출이 가능합니다!")
# else:
#     print("수익 창출이 불가능합니다!")

# minAvailable = "1000"
# inputValue = int(input("현재 구독자 수를 입력해 주세요: "))

# if int(1000) <= inputValue:
#     print("수익 창출이 가능합니다!")
# else:
#     print("수익 창출이 불가능합니다!")
# 조건문에서도 타입 캐스팅 가능함


"""
2. 윤행이는 평소 휴대폰을 너무 많이 사용해 공부시간을 다 빼앗기고 있었다.
이렇게 가면 얼마 남지 않은 기말고사를 망칠 게 뻔했다.
윤행이가 공부시간을 다 채울 경우에만 휴대폰을 사용할 수 있도록 프로그램을 만들어주자.

입력
공부시간을 입력해주세요(시간):

출력
10시간 이상이면 "휴대폰 잠금이 해제됩니다."
5시간 이상이면 "휴대폰을 30분간 사용가능합니다."
나머지 "휴대폰 사용이 불가능합니다."
"""

# studyTime = int(input("공부시간을 입력해주세요(시간):"))

# if studyTime >= 10:
#     print("휴대폰 잠금이 해제됩니다.")
# elif studyTime >= 5:
#     print("휴대폰을 30분간 사용가능합니다.")
# else:
#     print("휴대폰 사용이 불가능합니다.")


"""
3. 현동이는 강의를 8시간 동안 들으니, 배가 너무 고파 저녁을 먹기로 하였다. 
현동이가 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력해 주는 프로그램을 작성해 보자.

20000원 이상 : 치킨
10000원 이상 : 떡볶이
2000원 이상 : 편의점 김밥 

입력
현재 가진 금액을 입력:

치킨 : 오늘 저녁은...치킨이다!
떡볶이 : 오늘 저녁은...떡볶이다!
출력 : 오늘 저녁은...편의점 김밥ㅠ
"""

inputMoney = int(input("현재 가진 금액을 입력:"))

if inputMoney >= 20000:
    print("오늘 저녁은...치킨이다!")
elif inputMoney >= 10000:
    print("오늘 저녁은...떡볶이다!")
elif inputMoney >= 2000:
    print("오늘 저녁은...편의점 김밥ㅠ")
