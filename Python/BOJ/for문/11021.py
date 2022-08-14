import sys
t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%i: %s" %(i+1, a+b))

