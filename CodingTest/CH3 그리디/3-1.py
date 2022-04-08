# 거스름돈
n = int(input())
count = 0
coinArray = [500, 100, 50, 10]

for coin in coinArray:
    count += n//coin # 거스름돈을 coin으로 나누고 나온 몫
    n %= coin # n을 coin으로 나눈 나머지를 n에 대입

print(count)