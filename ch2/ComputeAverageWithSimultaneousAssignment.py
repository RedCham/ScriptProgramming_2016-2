# 사용자로부터 세 개의 숫자를 입력받는다.
number1, number2, number3 = eval(input(
  "세 개의 숫자를 콤마(,)로 구분하여 입력하세요: "))

# 평균을 계산한다.
average = (number1 + number2 + number3) / 3

# 결과를 출력한다.
print(number1, number2, number3,
    "의 평균은", average, "입니다.")
