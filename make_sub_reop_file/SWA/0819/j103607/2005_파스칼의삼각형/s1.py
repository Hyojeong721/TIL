import sys
sys.stdin = open('input.txt')



# def pascal(N):
#
#     triangle = []
#     if N == 1:
#         triangle.append([N])
#     if N == 2:
#         triangle.
#
# print(pascal(1))








T = int(input())
for tc in range(1, T + 1):

    # N = int(input())
    N = 5



    tri_list = []
    for i in range(N):
        for j in range(i):
            tri_list.append([1])
    print(tri_list)

    # for i in range(1, N):
    #     for j in range(1, N):
    #         board[i][j] = board[i-1][j-1] + board[i-1][j]
    # print(board)

