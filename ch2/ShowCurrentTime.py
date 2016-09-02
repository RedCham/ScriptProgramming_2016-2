import time

currentTime = time.time() # 현재 시간을 얻어온다.

# 1970년 1월 1일 자정 이후로의 전체 초 값을 얻어온다.
totalSeconds = int(currentTime)

# 현재 시간의 초 값을 계산한다.
currentSecond = totalSeconds % 60

# 전체 분 값을 계산한다.
totalMinutes = totalSeconds // 60

# 현재 시간의 분 값을 계산한다.
currentMinute = totalMinutes % 60

# 전체 시 값을 계산한다.
totalHours = totalMinutes // 60

# 현재 시간의 시 값을 계산한다.
currentHour = totalHours % 24

# 결과를 출력한다.
print("현재 시간은" + str(currentHour) + ":"
    + str(currentMinute) + ":" + str(currentSecond) + " GMT 입니다.")
