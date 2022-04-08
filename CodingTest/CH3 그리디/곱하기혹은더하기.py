s = list(map(int, input()))
result = 1

for i in s:
    if i != 0:
        result *= i

print(result)