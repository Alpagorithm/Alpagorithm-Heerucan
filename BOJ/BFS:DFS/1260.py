from collections import deque

n, m, v = map(int, input().split())

g = [[0] * (n + 1) for _ in range(n + 1)]
visited= [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1


def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for i in range(1, n+1):
        if not visited[i] and g[v][i] == 1:
            dfs(i)

def bfs(v):
    visited[v] = False
    queue = [v]
    while queue: # queue가 채워져있는 동안에만 해당 while문이 돌아감
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(n+1):
            if visited[i] and g[v][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(v)
print()
bfs(v)