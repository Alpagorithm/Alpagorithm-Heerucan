# 답안 참고함

n = int(input())
fear = list(map(int, input().split()))

fear.sort() # 공포도를 정렬하고 [1, 2, 2, 2, 3]

groupCount = 0 # 그룹의 수
traveler = 0 # 그룹에 현재 포함된 모험가 수

# 먼저 공포도가 가장 큰 사람한테 배치
# 공포도사람 <= 팀원수

for i in fear:
    traveler += 1
    if traveler >= i: # 현재 모험가 수 >= 공포도 -> 그룹 결성
        groupCount += 1
        traveler = 0 # 그리고 다시 그룹을 초기화 시킴

print(groupCount)