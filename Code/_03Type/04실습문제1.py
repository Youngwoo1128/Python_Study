"""
실습문제 9
다음 연산의 결과를 예상해 보세요
result = 100 + 20 / (4 - 2) * 5
답 : 100.0 
틀림 ㅋㅋㅋㅋㅋ 자만 x
답 : 150.0
자바랑 같이 ()괄호 안이 우선연산이 되고 그다음 *, / 그다음 + 연산
"""
from email.policy import default


result = 100 + 20 / (4 - 2) * 5
print(result)

"""
정리 
파이썬의 연산 우선 순위
1. 괄호
2. 지수 (지수 : **, 사전적 의미: 어떤 수나 문자의 오른쪽 위에 덧붙여 쓰여 그 거듭제곱을 한 횟수를 나타내는 문자나 숫자.)
3. 곱셉, 나눗셈, 몫, 나머지
4. 덧셈, 뺄셈
5. 같은 우선 순위 에서는 왼쪽 -> 오른쪽
"""

"""
실습문제 10
머쓱이느 편의점 아르바이트를 하고 있습니다.
시급, 일일 근무시간, 한달 동안 일한 날의 수, 이번달 보너스가 입력으로 주어질 때, 머쓱이의 이번달 급여를 출력하는 코드를 작성해보세요
"""
#시급
timePrice = int(input())

#일일 근무시간
perTime = int(input())

#한달 동안 일한 날의 수
perMonth = int(input())

#보너스
bonus = int(input())

myPay = (perTime * timePrice) * perMonth + bonus
print(myPay) #결과 850000

"""
여기서 중요한거
type casting
입력 값을 type casting 하는법
원하는 자료형 자료형(input)
boolean 으로 정수를 받는다면??
놀랍게도 True
"""
booleanCasting = bool(input())
print(booleanCasting)

"""
그러면
input을 type casting 하지않고 연산을 한다면??
일단 default 부터
일단 default는 String

defaultType= input()
print(type(defaultType)) 

아까 잠깐 해봤을떄는 string 끼리는 연산이 안됐음
그래도 일단 해보기

default1 = input()
default2 = input()
일떄 + 는 된다.
하지만 - 는 안된다. 
print(default1 - default2)

한가지 간과한게,,,
string1 = "안"
string2 = "녕"
print(string1 + string2)
하면 안녕 이라고 나왔었고
강의 완전 초반에 String 끼리 결합 할때 이 방법을 강의 한적이 있으심
"""

"""
그럼 input을 문자열로 입력하고 int로 type casting을 한다면?

inputString = int(input())
print(inputString)
print(type(inputString))

input 값을 안녕이라고 해봤음
결과 -> ValueError: invalid literal for int() with base 10: '안녕'
"""

"""
실습문제 11
중간고사를 치른 머쓱이는 자신의 평균점수가 궁금해졌습니다.
영어, 수학, 국어, 과학 점수가 입력으로 주어질 때, 중간고사 평균 점수를 출력하는 코드를 완성해보세요.

각각 70, 80, 60, 100 으로 입력 했을떄 예상결과
310 / 4
77.5

"""
english = int(input("영어:"))
math = int(input("수학:"))
korean = int(input("국어:"))
science = int(input("과학:"))
average = (english + math + korean + science) / 4
print(average)