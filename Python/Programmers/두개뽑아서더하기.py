# level1 프로그래머스
# 구현

def solution(numbers):
    answer = []
    sum = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                sum = numbers[i] + numbers[j]
                answer.append(sum)
    return list(sorted(set(answer)))