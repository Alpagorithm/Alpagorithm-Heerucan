# 삽입정렬 소스코드

lists = [8, 3, 2, 7, 6]

for i in range(1, len(lists)):
    j = i
    while j > 0 and lists[j-1] > lists[j]:

        lists[j-1], lists[j] = lists[j], lists[j-1]
        j -= 1

print(lists)

