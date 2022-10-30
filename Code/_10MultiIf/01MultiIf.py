"""
다중 조건문
그냥 똑같다.
"""

"""
대현이는 S사 공개채용에 지원했다.
공개채용 과정은 필기시험을 80점 이상 받아야, 면접을 볼 수 있다.
그리고 면접에서 pass를 할 경우 최종합격된다.
프로그램 사용자로부터 필기시험 점수를 먼저 입력받고 890점 이상인 경우 면접 결과를 입력받는다.
(80점 미만일 경우 바로 불합격을 출력) 면접 결과가 pass인 경우 최종합격을 출력한다. fail 일 경우 불합격을 출력한다.

입력
필기시험 점수를 입력하세요:80
면접결과를 입력하세요:pass

출력 최종합격

입력 필기시험 점수를 입력하세요:70

츨력 불합격
"""

# writtenTest = int(input("필기시험 점수를 입력하세요:"))

# if writtenTest < 80:
#     print("불합격")

# interviewTest = str(input("면접결과를 입력하세요:"))
# if interviewTest == "pass":
#     print("최종합격")

# 틀림 

# 다시 풀어보기

writtenTest = int(input("필기시험 점수를 입력하세요:"))

if writtenTest < 80:
    print("불합격")
else :
    interviewTest = str(input("면접결과를 입력하세요:"))
    if interviewTest == "pass":
        print("최종합격")
    else:
        print("불합격")