import sys
n = int(input())

data = [0]*n
for i in range(n):
    data[i] = int(sys.stdin.readline().rstrip())

data.sort()
for i in range(len(data)):
    print(data[i], end='\n')