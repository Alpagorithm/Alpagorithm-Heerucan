# 2309 백준 브론즈1
# 정렬, 브루트포스

from itertools import combinations

data = [] # 전체 9명 난쟁이
exceptData = [] # 2명 난쟁이

for i in range(9):
    data.append(int(input()))

# 더해서 result가 되는 난쟁이들만 빼주면 됨
result = sum(data) - 100

for i in combinations(sorted(data), 2):
    if sum(i) == result:
        exceptData = list(i)

# 9명 난쟁이에서 2명의 가짜 난쟁이를 뺀 배열
for i in [x for x in sorted(data) if x not in exceptData]:
    print(i)

