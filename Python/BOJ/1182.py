# 백준 1182 실버3
# 부분수열의 합
# 브루트포스 알고리즘, 백트래킹

from itertools import combinations

n, s = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
count = 0

for i in range(1, n+1):
    for j in combinations(data, i):
        # print("순열들: ", j, " / 합 = ", sum(j))
        if sum(j) == s:
            count += 1

print(count)




