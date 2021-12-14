h, m = map(int, input().split())

if m >= 45:
    m = m - 45
    print(h, m)
else:
    m = m - 45
    m = 60 + m
    if h > 0:
        h = h-1
        print(h, m)
    else:
        print(23, m)