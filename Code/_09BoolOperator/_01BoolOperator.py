"""
파이썬의 논리 연산은
and 는 and
or 은 or
not 은 not
뭐 더 이상 할 말이 없음
"""

"""
바로 실습문제로 
1. 민아는 유튜브를 통해 수익창출을 하려고 한다.
기존에는 구독자가 1000명만 넘으면 수익창출이 가능ㄹ했는데,
시청시간 4000시간까지 넘어야지 수익창출이 가능해졌다.
프로그램 사용자로부터 현재 구독자수와 시청시간을 입력 받으면, 수익창출이 가능한지 불가능한지 알려주는 프로그램을 작성해보자. (수익창출은 구독자 1000명이상, 시청시간 4000시간 이상 가능)


입력
현재 구독자 수:1200
시청시간: 4500

출력
수익 창출 가능
"""

# subsNumber = int(input("현재 구독자 수:"))
# watchingTime = int(input("시청시간:"))

# if subsNumber >= 1000 and watchingTime >= 4000:
#     print("수익 창출 가능")
# else:
#     print("수익 창출 불가능") 


"""
2. 스타트코딩학교에서 체력검정을 실시한다. 종목은 팔굽혀펴기, 윗몸일으키기, 턱걸이 3가지 이다.
3가지를 모두 측정하는데 그 중 1가지라도 합격권에 들면 pass 이다.
3가지 종목이 입력으로 주어 질때, pass 인지 fail인지 알려주는 프로그램을 작성해보자.(팔굽혀펴기는 30개이상, 윗몸일으키기는 35개이상, 턱걸이는 5개이상 합격권)

입력
팔굽혀펴기:5
윗몸일으키기:15
턱걸이:0

fail
"""

pushUpCount = int(input("팔굽혀펴기:"))
sitUpCount = int(input("윗몸일으키기:"))
chinUpsCount = int(input("턱걸이"))

if pushUpCount >= 30 or sitUpCount >= 35 or chinUpsCount >= 5:
    print("pass")
else:
    print("fail")