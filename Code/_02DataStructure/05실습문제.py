"""
실습문제 5
다음 문자열 데이터를 변수에 저장하고 출력해보세요.
"South Korea"
"Seoul"
"Gang-nam"
"""
southKorea = "South Korea"
seoul = "Seoul"
gangNam = "Gang-nam"
# print(southKorea)
# print(seoul)
# print(gangNam)
# 혹은
print(southKorea, seoul, gangNam, sep="\n")

"""
실습문제 6
다음과 같이 화면에 출력하도록 코드를 완성해 보세요.
지금 까지 배운내용을 모두 활용해 봅니다. (변수, 문자열, 여러 항목 출력, 문자열 연산)

Best Pop Songs
Justin Bieber-Off My Face
Charlie Puth-That's Hilarious
"""

bestPopSong = "Best Pop Songs \nJustin Bieber-Off My Face \nCharlie Puth-That's Hilarious"
print(bestPopSong)

"""
실습문제7
이름을 사용자로 부터 입력 받아서 환영 메시지를 완성해 봅니다.

입력
종현

출력
안녕하세요.종현님 환영합니다!!
"""

userName = input()
# print("안녕하세요." + userName +"님 환영합니다!!")
# 틀림 -> 띄워쓰기 안함
print("안녕하세요.", userName + "님 환영합니다!!")

"""
이름, 나이를 사용자로부터 입력 받아서 출력문을 완성해 봅시다.

입력
이름을 입력하세요:현동
나이를 입력하세요:30
"""
yourName = input("이름을 입력하세요:")
yourAge = input("나이를 입력하세요:")
print("제 이름은", yourName + "입니다.")
print("나이는", yourAge + "살 입니다.")