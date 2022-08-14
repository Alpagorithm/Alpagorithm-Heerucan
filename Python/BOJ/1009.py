import sys

t = int(input())

for _ in range(t):
    a, b = list(map(int, input().split()))
    print(a**b%10)
