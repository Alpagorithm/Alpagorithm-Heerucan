n = int(input())

result = 1
if n == 0:
    print(1)
else:
    for i in range(n, 0, -1):
        result *= i
    print(result)