from collections import deque

a, b = map(int, input().split())

graph = []

for i in range(a):
    graph.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= a or ny < 0 or ny >= b:
                continue

            if graph[nx][ny] == 0: # 0은 이동할 수 없는 칸
                continue

            if graph[nx][ny] == 1: # 1은 이동할 수 있는 칸
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[a-1][b-1]

print(bfs(0, 0))

