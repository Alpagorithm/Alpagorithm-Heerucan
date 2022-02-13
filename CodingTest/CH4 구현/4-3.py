# N 입력받기
n = list(input())

x = n[0]
y = n[1]
print(x, y)

# # 이동 방향
# dx = [2, 2, 1, 1, -1, -1, -2, -2]
# dy = [1, -1, 2, -2, 2, -2, -1, 1]
# #
# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
#
# print(x, y)