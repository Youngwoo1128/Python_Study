"""
제어문 종류
if, elif, else

if 조건:
    print()
"""
"""
진짜 중요한점
1. if 에 괄호 x
2. if의 조건 뒤에 : 콜론
3. 조건문 타는 곳에 space4칸 or "tab" 눌러야함
4. 괄호 없음 
"""

orgin_pass = 1234
input_pass = int(input("비밀번호 입력: "))

if orgin_pass == input_pass:
    print("로그인 성공!")
elif orgin_pass > input_pass:
    print("다시시도해주세요")
else:
    print("로그인 실패")
print("프로그램 종료")