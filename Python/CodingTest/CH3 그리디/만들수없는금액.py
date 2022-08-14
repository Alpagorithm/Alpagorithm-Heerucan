import itertools
# 5
# 3 2 1 1 9

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
print(coin)

for x in coin:
    if target < x:
        break
    target += x

print(target)