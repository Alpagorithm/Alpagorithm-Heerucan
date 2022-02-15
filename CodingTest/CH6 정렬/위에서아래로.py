N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

# 선택정렬
def selectionSorting(list):
    for i in range(len(list)):
        max = i
        for j in range(i+1, len(array)):
            if list[max] < list[j]:
                max = j
        list[i], list[max] = list[max], list[i]
    print(list)

selectionSorting(array)


# 삽입정렬
def insertSorting(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j-1] < list[j]:
            list[j-1], list[j] = list[j], list[j-1]
            j -= 1
    print(list)

insertSorting(array)


# 정렬 라이브러리 사용
array.sort(reverse=True)
print(array)