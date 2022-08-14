# 백준 9095 실버3
# 다이나믹 프로그래밍 : 1, 2, 3 더하기


t = int(input())
n = [int(input()) for i in range(t)]

dp = [0]*11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for j in range(len(n)):
    for i in range(4, n[j] + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n[j]])

