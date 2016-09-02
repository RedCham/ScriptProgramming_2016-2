# 연이율을 입력한다.
annualInterestRate = eval(input(
  "연이율을 입력하세요(예, 7.25): "))
monthlyInterestRate = annualInterestRate / 1200

# 상환년수를 입력한다.
numberOfYears = eval(input(
  "상환년수를 정수로 입력하세요(예, 5): "))

# 대출금을 입력한다.
loanAmount = eval(input("대출금을 입력하세요(예, 120000950: "))

# 총상환금을 계산한다.
monthlyPayment = loanAmount * monthlyInterestRate / (1
  - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

# 결과를 출력한다.
print(monthlyPayment)
print(int(monthlyPayment * 100))
print("월상환금은", int(monthlyPayment * 100) / 100, "입니다.")
print("총상환금은", int(totalPayment * 100) /100, "입니다.")
