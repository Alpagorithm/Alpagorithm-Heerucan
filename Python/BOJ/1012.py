import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x <= -1 or x>= n or y <= -1 or y >= m: # 방향 벗어나서 끝내
        return False
    if data[x][y] == 1: # 1은 배추 있는 곳 -> 지렁이도!
        data[x][y] = 0 

        for i in range(4):
            dfs(x + dx[i], y+dy[i])
        
        return True
    return False


T = int(input())

for i in range(T):
    m, n, k = map(int, input().split())  # M:가로, N:세로, K:개수
    data = [[0]*m for i in range(n)]
    cnt = 0

    for j in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1 # 왜 y부터 하냐면, 2차원배열에서 먼저 세로부터 구하게 됨

    # 이제 여기서 배추 지렁이 체크
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1

    print(cnt)

