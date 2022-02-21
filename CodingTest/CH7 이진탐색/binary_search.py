

# 이진 탐색 소스 코드 - 재귀함수

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target: # 왼쪽을 봐야지
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid+1, end)

# 이진 탐색 소스 코드 - 반복문

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
result2 = binary_search2(array, target, 0, n-1)

if result == None:
    print("찾는 원소 없음")
else:
    print("찾는 원소는", result+1,"번째")

if result2 == None:
    print("찾는 원소 없음")
else:
    print("찾는 원소는", result + 1, "번째")

