# 5
# R R R U D D
n = int(input())
direction = input().split()

x, y = 1, 1

for i in range(len(direction)):
    if direction[i] == 'R':
        if y == n:
            y += 0
        else:
            y += 1

    elif direction[i] == 'L':
        if y == 1:
            y += 0
        else:
            y -= 1

    elif direction[i] == 'U':
        if x == 1:
            x += 0
        else:
            x -= 1

    elif direction[i] == 'D':
        if x == n:
            x += 0
        else:
            x += 1


print(x, y)