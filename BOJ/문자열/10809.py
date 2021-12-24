# 답안 참고
s = list(input())
import string
alphabet = list(string.ascii_lowercase)

for i in alphabet:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')