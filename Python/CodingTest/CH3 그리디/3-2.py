# 큰 수의 법

n, m, k = map(int, input().split())
result = 0
data = list(map(int, input().split()))

data.sort()

while m > 0:
    for i in range(k):
        result += data[-1]
        m -= 1
    result += data[-2]
    m -= 1

print(result)
