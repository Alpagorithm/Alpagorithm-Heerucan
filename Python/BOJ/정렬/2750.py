n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

sortedA = sorted(a)

for i in range(len(sortedA)):
    print(sortedA[i])
