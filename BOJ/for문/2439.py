t = int(input())
a = ' '
b = '*'
for i in range(1, t+1):
    print('%s%s' %((a*(t-i)), (b*i)))