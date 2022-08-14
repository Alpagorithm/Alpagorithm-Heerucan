import sys
from itertools import combinations

n, m = list(map(int, input().split()))
k = list(map(int, sys.stdin.readline().split()))

count = 0
for i in combinations(k, 2):
    if i[0] != i[1]:
        count += 1

print(count)
