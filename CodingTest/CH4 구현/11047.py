n, k = list(map(int, input().split()))

coin = []
result = 0
for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in range(len(coin)):
    result += k // coin[i]
    k = k % coin[i]

print(result)


