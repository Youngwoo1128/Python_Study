import turtle as t

# as t
# 해당 라이브러리를 t로 사용할 수 있음

# 거북이 모양으로 변경
t.shape('turtle')

# 저 명령어만 쓰게 되면 화면이 켜졌다가 바로 꺼짐

# 거북이 색 변경
t.color('orange')
t.bgcolor('steelblue')

# 속도 조절 1 ~ 10
t.speed(1)

# 앞으로 가기 
t.forward(200)

# 방향 전환 (왼쪽으로 90도)
t.left(90)
t.forward(200)

# 특정 좌표로 이동
t.goto(0, 200)

# 펜 올리기
t.penup()
t.forward(-200)

# 화면을 클릭할 때 종료
t.exitonclick()