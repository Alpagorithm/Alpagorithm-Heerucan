# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    a.pop(0)
    a.append(b[i])

print(sum(a))
