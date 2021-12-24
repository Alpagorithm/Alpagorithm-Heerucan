n = 0
t = int(input())
while n<t:
    r, s = list(input().split())
    r = int(r)
    s = list(s)
    n += 1
    for i in range(len(s)):
        print(s[i]*r, end='')
    print()