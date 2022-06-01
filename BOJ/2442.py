# BOJ 2442 브론즈3
# 입출력 구현

n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i + '*' * (i-1))