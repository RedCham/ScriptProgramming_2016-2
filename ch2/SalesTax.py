# 사용자로부터 입력을 받는다.
purchaseAmount = eval(input("총 구입액을 입력하세요: "))

# 판매세를 계산한다.
tax = purchaseAmount * 0.06

# 판매세를 소수점 둘째자리까지 출력한다.
print("판매세는", int(tax * 100) / 100.0, "입니다.")
