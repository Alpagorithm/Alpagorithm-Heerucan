# 숫자 카드 게임

# n : 행의 개수
# m : 열의 개수

n, m = map(int, input().split())
minData = []
for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    data[0]
    minData.append(data[0])
minData.sort()
print(minData[-1])
