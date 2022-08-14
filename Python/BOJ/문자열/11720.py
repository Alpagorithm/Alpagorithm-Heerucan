import sys

n = int(input())
data = list(map(int, sys.stdin.readline().strip()))
print(sum(data))