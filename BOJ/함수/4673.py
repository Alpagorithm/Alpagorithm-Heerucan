def selfNumber():
    allNum = []  # 1~10000까지 리스트
    iSum = []  # 39 + 3 + 9 같은 걸 넣는 리스트
    for i in range(1, 10001):
        ilist = list(map(int, str(i)))  # 리스트화 시켜주기
        total = int(i) + sum(ilist)  # 39 + 3 + 9 해주기
        allNum.append(i)
        iSum.append(total)
    initialNum = sorted(list(set(allNum) - set(iSum)))  # 리스트 정렬해서 반환

    for i in range(len(initialNum)):
        print(initialNum[i])

selfNumber()