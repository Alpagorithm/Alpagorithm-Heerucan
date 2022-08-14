a, b = map(int, input().split())
c = int(input())

if (b+c) >= 60:
    if (b+c) % 60 >= 0:
        a += (b+c)//60
        b = (b+c)-(60*((b+c)//60))
        if a >= 24:
            # a = 0
            a = a - 24
    else:
        a += 1
        b = (b+c - 60)
        if a >= 24:
            a = a - 24
            a = 24 - a
    print(a, b)
else:
    print(a, b+c)



