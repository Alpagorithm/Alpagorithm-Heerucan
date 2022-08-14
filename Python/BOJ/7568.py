# 백준 7568 실버5.. 에.. 참고했음..
# 구현, 브루트포스
# 덩치

import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))


for i in data:
    rank = 1
    for n in data:
        if i[0] < n[0] and i[1] < n[1]:
            rank += 1
    print(rank, end =' ')



