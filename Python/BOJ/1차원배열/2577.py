a = int(input())
b = int(input())
c = int(input())

n = list(map(int, str(a*b*c)))
for i in range(10):
    print(n.count(i))

