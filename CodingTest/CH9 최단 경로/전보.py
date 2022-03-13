import heapq
import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]

INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해서 큐에 삽입
    heapq.heappush(q, (0, start))
    # 자기자신한테 가는 거리는 0으로 설정
    distance[start] = 0

    while q: # 큐가 비어있지 않으면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
time = []

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 무한과 자기자신이 아닌 경우
    if distance[i] != INF and distance[i] != 0:
        count += 1
        time.append(distance[i])

print(count, max(time))




