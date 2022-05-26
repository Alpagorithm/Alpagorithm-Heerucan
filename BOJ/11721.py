# BOJ 브론즈2 11721
# 열 개씩 끊어 출력하기

n = input()
cnt = 0

for i in n:
    print(i, end="")
    cnt += 1
    if cnt % 10 == 0:
        print()