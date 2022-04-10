# food_times 배열
# k초가 매개변수
# 답 참고해서 리팩...ㅠㅠ
import heapq

food_times1 = list(map(int, input().split()))
k1 = int(input())

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 우선순위큐(최소힙)에다가 삽입
    # 음식 번호와 시간을 튜플형태로 삽입, 시간을 기준으로 최소힙 완성됨
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    # q [(1초, 2번), (2초, 3번), (3초, 1번)]

    food_num = len(food_times)  # 남은 음식의 개수
    previous = 0  # 이전 음식을 먹는데 걸리는 시간

    while True:
        # 먹는데 걸리는 시간 = 음식을 먹는 시간 * 남은 음식의 개수
        time = (q[0][0]-previous)*food_num

        # 중단 시간 >= 먹는데 걸리는 시간
        if k >= time:
            k -= time
            food_num -= 1
            previous = heapq.heappop(q)[0]

        # 중단 시간 <= 먹는데 걸리는 시간
        else:
            i = k % food_num
            q.sort(key=lambda x: x[1])  # 음식 번호로 정렬
            return q[i][1]


solution(food_times1, k1)