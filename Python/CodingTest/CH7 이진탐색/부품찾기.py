# 5
# 8 3 7 9 2
# 3
# 5 7 9

n = int(input())
store = list(map(int, input().split()))
store.sort() # 꼭 정렬해줘야만 이진탐색을 사용 가능!!!!!
m = int(input())
user = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in range(m):
    result = binary_search(store, user[i], 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')



