# n:  집(노드) m: 길(간선)
# 유지비의 합을 최소로 -> 신장트리 바이브

# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선 개수 입력받기
n, m = map(int, input().split())
parent = [0]*(n+1) #부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge # edge에 cost, a, b 값을 넣어줌
    # 사이클이 발생하지 않는 경우에만 집합에 포함 - 최소한의 길만 만드는 것
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        print(result, cost)
        totalResult = result - cost # 마지막 값 빼주기

print(totalResult)
