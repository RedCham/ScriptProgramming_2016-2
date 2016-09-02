import turtle

# 사용자로부터 두 점을 입력받는다.
x1, y1 = eval(input("첫번째 점에 대한 x1과 y1을 입력하세요: "))
x2, y2 = eval(input("두번째 점에 대한 x2와 y2를 입력하세요: "))

# 거리를 계산한다.
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# 두 점을 연결하는 직선을 그린다.
turtle.penup()
turtle.goto(x1, y1) # (x1, y1)로 이동한다.
turtle.pendown()
turtle.write("점 1")
turtle.goto(x2, y2) # (x2, y2)까지 직선을 그린다.
turtle.write("점 2")

# 직선 중앙으로 이동한다.
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.done()
