# 2562
import sys

n = []
for i in range(9):
    a = int(sys.stdin.readline())
    n.append(a)

print(max(n))
print(int(n.index(max(n)))+1)