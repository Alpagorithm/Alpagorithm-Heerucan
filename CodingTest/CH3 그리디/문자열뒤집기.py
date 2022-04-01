s = list(map(int, input()))
count = 0
for i in range(len(s)):
    if s[i-1] != s[i]:
        count += 1

print(count//2)


