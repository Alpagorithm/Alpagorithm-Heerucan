import sys

n = int(input())
score = list(map(int, sys.stdin.readline().split()))
newScore = 0
maxScore = max(score)
for i in range(len(score)):
    score[i] = float(score[i])/float(maxScore)*100
    newScore += score[i]
print(newScore/n)
