
# 3052
rest = []
b = 0
for i in range(10):
    a = int(input())
    n = a%42
    rest.append(n)

print(len(set(rest)))