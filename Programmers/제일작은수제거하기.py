# 프로그래머스 level1
# 제일 작은 수 제거하기

data = [3, 10, -1, 0]

# print(sorted(data))

def solution(arr):
    answer = []
    if len(arr) == 1:
        answer = [-1]
        print(answer)
    else:
        arr.remove(sorted(arr)[0])
        answer = arr
        print(answer)
    return answer

solution([1, -1, 3, 0])