import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    # # 가로 검토
    # for i in range(N):
    #     check = 0
    #     for j in range(N):
    #         if puzzle[i][j] == 0:
    #             if check == K:
    #                 count += 1
    #             check = 0
    #             continue
    #         else:
    #             check += 1
    #     if check == K:
    #         count += 1
    # # 세로 검토
    # for i in range(N):
    #     check = 0
    #     for j in range(N):
    #         if puzzle[j][i] == 0:
    #             if check == K:
    #                 count += 1
    #             check = 0
    #             continue
    #         else:
    #             check += 1
    #     if check == K:
    #         count += 1
    #
    # print('#{} {}'.format(test_case, count))

#
# # import sys
# # sys.stdin = open('input.txt')
# #
# # T = int(input())
# #
# # for test_case in range(1, T + 1):
# #
# #     N, K = list(map(int, input().split()))
# #     board = [list(map(int, input().split())) for _ in range(N)]
# #
# #     word_afford = []
# #
# #     #전에 했던 row합, column합 응용이다. 쭉 더하다 0나오면 스탑
# #
# #     #row
# #     for i in range(N):
# #         afford = 0
# #         for j in range(N):
# #             if board[i][j] != 0:
# #                 afford += 1
# #                 if j == N - 1:
# #                     word_afford.append(afford)
# #             else:
# #                 if afford != 0:
# #                     word_afford.append(afford)
# #                 afford = 0
# #
# #     #column
# #     for i in range(N):
# #         afford = 0
# #         for j in range(N):
# #             if board[j][i] != 0:
# #                 afford += 1
# #                 if j == N - 1:
# #                     word_afford.append(afford)
# #             else:
# #                 if afford != 0:
# #                     word_afford.append(afford)
# #                 afford = 0
# #     count = 0
# #
# #     #단순비교
# #     for number in word_afford:
# #         if K == number:
# #             count += 1
# #     print('#{} {}'.format(test_case, count))


# import sys
#
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, K = list(map(int, input().split()))
#     puzzle = [list(map(int, input().split())) for _ in range(N)]
#     result = 0  # 단어가 들어갈 수 있는 자리수
#     tmp = 0  # 연속된 1의 갯
#     i = 0
#     j = 0
#     # 가로로 찾는 경우
#     while 0 <= i < N and 0 <= j < N:
#         # 값이 0이라면 다음 칸으로 이동, tmp 초기화
#         if puzzle[i][j] == 0:
#             j += 1
#             tmp = 0
#
#         # 값이 1인 경우
#         elif puzzle[i][j] == 1:
#             # 범위를 퍼즐로 한정, 연속된 1의 갯수를 tmp에 할당
#             while j < N and puzzle[i][j] == 1:
#                 tmp += 1
#                 j += 1
#         # tmp의 값이 단어의 길이와 같은 경우 result += 1
#         if tmp == K:
#             result += 1
#
#         # 마지막 칸에 도착 한 경우 아랫 줄로 이동하며 j, tmp 값 초기화
#         if j == N:
#             i += 1
#             j = 0
#             tmp = 0
#
#     # 초기화
#     tmp = 0
#     i = 0
#     j = 0
#     # 세로로 찾는 경우(위와 동일)
#     while 0 <= i < N and 0 <= j < N:
#         if puzzle[i][j] == 0:
#             i += 1
#             tmp = 0
#         elif puzzle[i][j] == 1:
#             while i < N and puzzle[i][j] == 1:
#                 tmp += 1
#                 i += 1
#
#         if tmp == K:
#             result += 1
#
#         if i == N:
#             j += 1
#             i = 0
#             tmp = 0
#
#     print('#{} {}'.format(tc, result))


    for i in range(N):
        check = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                check += 1
            else:
                if check == K:
                    count += 1
                    check = 0
                else:
                    check = 0
        if check == K:
            count += 1

    for j in range(N):
        check = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                check += 1
            else:
                if check == K:
                    count += 1
                    check = 0
                else:
                    check = 0
        if check == K:
            count += 1

    print('#{} {}'.format(test_case, count))


