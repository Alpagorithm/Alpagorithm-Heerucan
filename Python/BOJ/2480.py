a, b, c = list(map(int, input().split()))
data = []
data.append(a)
data.append(b)
data.append(c)

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(data) * 100)