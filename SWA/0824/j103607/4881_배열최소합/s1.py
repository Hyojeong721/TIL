import sys
sys.stdin = open('input.txt')


'''
못 하겠음...
'''

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = []
    for i in range(N):
        for j in range(N):
            minV = board[i][0]
            if minV >= board[i][j]:
                minV = board[i][j]
                col = j
                visited.append(col)
                total_list.append(minV)
                print(total_list)

    #
    print(total)

