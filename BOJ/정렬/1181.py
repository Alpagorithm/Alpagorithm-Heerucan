import sys

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = sys.stdin.readline().rstrip()

setA = set(a)
a = sorted(setA)
a.sort(key = len)

for i in range(len(a)):
    print(a[i])