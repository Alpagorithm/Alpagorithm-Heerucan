n = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0
data = []
for i in range(n):
    result += p[i]
    data.append(result)
print(sum(data))
