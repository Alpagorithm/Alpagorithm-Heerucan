n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

d = [0]*301 # 0번째는...

d[1] = data[0]
d[2] = max(data[1]+data[0], data[2]+data[0]) # 30 / 25
d[3] = max(d[2]+data[2], d[2]+data[3])

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2])

print(d[3], data[2])