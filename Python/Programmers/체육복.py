# 풀이 참고
def solution(n, lost, reserve):
    # 여벌교복 가져온 학생도 도난 당할 수 있어서 중복삭제
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)

    for i in reserveSet:
        if i - 1 in lostSet:
            lostSet.remove(i - 1)
        elif i + 1 in lostSet:
            lostSet.remove(i + 1)
    return n - len(lostSet)