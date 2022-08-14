# 10972 백준 실버3 다음 순열
# 수학, 조합론
# 해설참고

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if array[i-1] < array[i]:
        for j in range(n-1, 0, -1):
            if array[i-1] < array[j]:
                array[i-1], array[j] = array[j], array[i-1]
                array = array[:i] + sorted(array[i:])
                print(*array)
                exit()

print(-1)
