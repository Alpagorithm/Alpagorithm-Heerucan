# 같은 팀 여부 확인
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n번, m개 연산
n, m = map(int, input().split())
parent = [0]*(n+1) #부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
