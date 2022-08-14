
data = []
a, b = map(int, input().split())

data = []
for i in range(a):
    data.append(list(map(int, input())))

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= a or y <= -1 or y >= b:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if data[x][y] == 0:
        # 해당 노드 방문 처리
        data[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(a):
    for j in range(b):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
        print(i,j,dfs(i, j), result)

print(result)