money = int(input("교환할 돈은 얼마 ? "))

remain_money = money

won_500 = (money//500)
#500원 계산
remain_money %= 500
#잔돈 계산
won_100 = remain_money//100
#100원 계산
remain_money %= 100
#잔돈 계산
won_50 = remain_money//50
#50원 계산
remain_money %= 50
#잔돈 계산
won_10 = remain_money//10
#10원 계산
remain_money %= 10
#잔돈 계산


print("500원짜리 ==> %d개" % won_500)
print("100원짜리 ==> %d개" % won_100)
print("50원짜리 ==> %d개" % won_50)
print("10원짜리 ==> %d개" % won_10)
print("바꾸지 못한 잔돈 ==> %d원" % remain_money)
#출력
