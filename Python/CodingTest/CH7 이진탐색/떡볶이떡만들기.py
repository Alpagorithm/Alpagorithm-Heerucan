# 4 6
# 19 15 10 17

import sys

n, m = list(map(int, input().split())) # 떡의 개수, 원하는 떡 길이
# array = sys.stdin.readline().rstrip()
array = list(map(int, input().split())) # 떡 개별 높이
array.sort() # 이진탐색을 위해 정렬


def binary_search(array, start, end):
    result = 0
    while m != result:
        mid = (start + end) // 2
        for i in range(len(array)):
            if array[mid] < array[i]:
                result += (array[i] - array[mid])
            else:
                result += 0
        print(array[mid])

binary_search(array, 0, n-1)
