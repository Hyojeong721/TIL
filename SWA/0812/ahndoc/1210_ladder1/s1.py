import sys
sys.stdin = open('input.txt', 'r')


# def search(start):
#     i = 99  # 행
#     j = start  # 열
#     while i > 0:  # 맨 윗줄에 도착하기 전까지 위로 올라감
#         i -= 1  # 위로 한 칸 이동
#         if j > 0 and data[i][j - 1] == 1: # 왼쪽 칸이 있고 1이면
#             while j > 0 and data[i][j - 1] == 1: # 사다리를 벗어나거나 0일 때까지
#                 j -= 1                           # 왼쪽 이동
#         elif j < 99 and data[i][j + 1] == 1: # 오른쪽 칸이 있고 1이면
#             while j < 99 and data[i][j + 1] == 1:
#                 j += 1                       # 오른쪽 이동
#         # 좌우가 0 이면 위로
#     return j   # 0번 행에 도착했을 때의 열(출발지) 리턴


T = 10
for tc in range(1, T + 1):
    t = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]


    # for j in range(100):
    #     if data[99][j] == 2:
    #         break
    #
    # # print(search(j))
    #
    # i = 99
    # while i > 0:
    #     if (0 <= j-1) and data[i][j-1] == 1:
    #         data[i][j] = -1
    #         j -= 1
    #     elif (j+1 < 100) and data[i][j+1] == 1:
    #         data[i][j] = -1
    #         j += 1
    #     else:
    #         i -= 1
    # print(j)

###################################################################
    # mode = 'up'
    # while i > 0:
    #     if mode == 'up':
    #         if 0 <= j-1 < 100 and data[i][j-1] == 1:
    #             j -= 1
    #             mode = 'left'
    #         elif 0 <= j+1 < 100 and data[i][j+1] == 1:
    #             j += 1
    #             mode ='right'
    #         else:
    #             i -= 1
    #     elif mode == 'left':
    #         if data[i-1][j] == 1:
    #             i -= 1
    #             mode = 'up'
    #         else:
    #             j -= 1
    #     else:
    #         if data[i-1][j] == 1:
    #             i -= 1
    #             mode ='up'
    #         else:
    #             j += 1
    # print(j)
#######################################################
    # i = 99
    # for j in range(100):
    #     if data[99][j] == 2:
    #         break
    #
    # while i > 0:
    #     if j == 0:
    #         if data[i][j+1] == 1:
    #             data[i][j] = -1
    #             j += s1
    #         elif data[i-1][j] == 1:
    #             data[i][j] = -1
    #             i -= 1
    #     elif j == 99:
    #         if data[i][j-1] == 1:
    #             data[i][j] = -1
    #             j -= 1
    #         elif data[i-1][j] == 1:
    #             data[i][j] = -1
    #             i -= 1
    #     else:
    #         if data[i][j+1] == 1 and j < 99:
    #             data[i][j] = -1
    #             j += 1
    #
    #         elif data[i][j-1] == 1 and j > 0:
    #             data[i][j] = -1
    #             j -= 1
    #
    #         elif data[i-1][j] == 1:
    #             data[i][j] = 1
    #             i -= 1
    # print('#{} {}'.format(t, j))
#######################################################

    for j in range(100):
        if data[99][j] == 2:
            break
    i = 99
    while i > 0:
        while j < 99 and data[i][j+1] == 1:
            data[i][j] = -1
            j += 1

        while j > 0 and data[i][j - 1] == 1:
            data[i][j] = -1
            j -= 1
        i -= 1

    print('#{} {}'.format(tc, j))





