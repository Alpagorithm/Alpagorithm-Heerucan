def findHansoo():
    n = int(input())
    count = 0

    for i in range(1, n + 1):
        if i < 100:
            count += 1
        else:
            ilist = list(map(int, str(i)))
            if ilist[0] - ilist[1] == ilist[1] - ilist[2]:
                count += 1
    print(count)

findHansoo()