"""
문자열 String
파이썬에서 문자열을 표기하는 방법은 "" 이나 ''으로 한다.
하지만 이 둘의 차이점이 있음

해당 문자열에서 구분하기 위함
이게 무슨말이냐 하면
"He was thinking, 'i am hungry...'" -> 여기의 시작과 끝은 ""
'She says, "I am hungry!"' -> 여기의 시작과 끝은 ''
"""

"""
또다른 이유는 escape 때문임
"""
# print("He was thinking, \'i am hungry...'\")
# error -> \ 위치 오류 아래처럼 위치 해야함 

print("He was thinking, \'i am hungry...\'")
# 결과 -> He was thinking, 'i am hungry...'