# 2
# 홍길동 95
# 이순신 77

N = int(input())
student = []

for i in range(N):
    student.append(list((input().split())))

sortedStudent = sorted(dict(student).items())

for i in range(len(sortedStudent)):
    print(sortedStudent[i][0], end= ' ')
