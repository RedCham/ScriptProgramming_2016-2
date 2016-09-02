# 사용자로부터 입력을 받는다.
seconds = eval(input("초 값을 정수로 입력하세요: "))

# 분 값과 나머지 초 값을 얻는다.
minutes = seconds // 60     # 초 단위의 시간에서 분 값을 계산한다.
remainingSeconds = seconds % 60   # 나머지 초 값을 계산한다.
print(seconds, "초는", minutes,
  "분과", remainingSeconds, "초입니다.")
