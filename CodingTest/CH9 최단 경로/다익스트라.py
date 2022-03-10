import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드, 간선 개수 입력받기
n, m = map(int, input().split())

# 노드 시작 번호 입력받기
start = int(input())

# 노드-노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)] # n이 3인 경우 [[], [], [], []]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b노드로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해서 큐에 삽입
    heapq.heappush((q, (0, start)))
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
            cost = dist + [1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF
        print("무한")
    else:
        print(distance[i])
