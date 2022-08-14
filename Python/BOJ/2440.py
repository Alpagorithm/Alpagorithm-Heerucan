n = int(input())

while n != 0:
    for i in range(n+1, 1, -1):
        print('*', end='')
    print()
    n -= 1