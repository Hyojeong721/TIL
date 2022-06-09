import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0]*10 for _ in range(10)]

    # N = number of columns

    # get color matrix
    info = [list(map(int, input().split())) for _ in range(N)]
    # [[1, 2, 3, 3, 1], [3, 6, 6, 8, 1], [2, 3, 5, 6, 2]]

    for n in range(N):
        # paint color
        for i in range(info[n][0], info[n][2]+1):
            for j in range(info[n][1], info[n][3]+1):
                matrix[i][j] += info[n][4]

    # count color 'purple'
    cnt_purple = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 3:
                cnt_purple += 1

    print("#{} {}".format(tc, cnt_purple))


