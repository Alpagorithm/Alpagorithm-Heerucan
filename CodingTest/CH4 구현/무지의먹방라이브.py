# food_times 배열
# k초가 매개변수
import heapq

food_times1 = list(map(int, input().split()))
k1 = int(input())


def solution(food_times, k):
    answer = -1
    if sum(food_times) <= k:
        return answer
    while k >= 0:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            else:
                k -= 1
                heap = []
                food_times[i] -= 1
                heapq.heappush(heap, food_times[i])
                if k == -1:
                    answer = i + 1
    return answer


solution(food_times1, k1)