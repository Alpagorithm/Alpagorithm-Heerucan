# BOJ 브론즈3 2522
# 입출력

n = int(input())

for i in range(0, n + 1):
    print(' ' * (i) + '*' * (n-i))