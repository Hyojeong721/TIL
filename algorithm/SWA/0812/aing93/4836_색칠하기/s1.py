import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for test_case in range(1, T + 1):
#
#     case = int(input())
#
#     board = [[0 for col in range(10)] for row in range(10)]
#
#     answer = 0
#
#     for i in range(case):
#         color = list(map(int, input().split()))
#         for j in range(color[0], color[2] + 1):
#             for k in range(color[1], color[3] + 1):
#                 if board[j][k] == 0:
#                     board[j][k] = color[4]
#                 else:
#                     if board[j][k] != color[4]:
#                         answer += 1
#
#     print('#{} {}'.format(test_case, answer))

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     red = [[0] * 10 for _ in range(10)]
#     blue = [[0] * 10 for _ in range(10)]
#     cnt = 0
#     for n in range(N):
#         lst = list(map(int, input().split()))
#
#         if lst[-1] == 1:
#             for i in range(lst[0],lst[2]+1):
#                 for j in range(lst[1],lst[3]+1):
#                     red[i][j] = 1
#         else:
#             for i in range(lst[0], lst[2] + 1):
#                 for j in range(lst[1], lst[3] + 1):
#                     blue[i][j] = 1
#     for r in range(10):
#         for c in range(10):
#             if red[r][c] == 1 and blue[r][c] == 1:
#                 cnt += 1
#
#     print('#{} {}'.format(tc, cnt))

# 색칠하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    red = [[0] * 10 for _ in range(10)]
    blue = [[0] * 10 for _ in range(10)]
    cnt = 0
    for n in range(N):
        lst = list(map(int, input().split()))
        if lst[-1] == 1:
            for i in range(lst[0], lst[2]+1):
                for j in range(lst[1], lst[3]+1):
                    red[i][j] = 1
        else:
            for i in range(lst[0], lst[2] + 1):
                for j in range(lst[1], lst[3] + 1):
                    blue[i][j] = 1

    for r in range(10):
        for c in range(10):
            if red[r][c] == 1 and blue[r][c] == 1:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

