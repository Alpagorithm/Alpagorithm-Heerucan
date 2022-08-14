n, m = map(int, input().split(' '))
data = []

def dfs(select, n, m):
    # 리스트에 들어간 수열들이 m개가 되면 리스트에 들어간 숫자들을 모두 출력하고 함수를 나온다.
    if len(data) == m:
        print(' '.join(map(str, data)))
        return
    for i in range(n):
        data.append(i+1)
        dfs(len(data)+1, n, m)
        data.pop()

dfs(0, n, m)
