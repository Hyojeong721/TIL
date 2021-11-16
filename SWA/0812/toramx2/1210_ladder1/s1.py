import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    test_case = int(input())

    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    di = [-1, 0, 0]
    dj = [0, -1, 1]
    k = 0
    i, j = 0, 0

    for row in range(100):
        for col in range(100):
            if arr[row][col] == 2:
                i, j = row, col

    while i > 0:
        # ni = i + di[k]
        # nj = j + dj[k]
        if j in range(100):
            if k == 0 and arr[i-1][j] == 1:
                if j-1 >= 0:
                    if arr[i][j - 1] == 1:
                        k = 1
                        # i, j = i + di[k], j + dj[k]
                    elif arr[i][j + 1] == 1:
                        k = 2
                        # i, j = i + di[k], j + dj[k]
                    else:
                        k = 0
                        # i, j = i + di[k], j + dj[k]
                else:
                    if arr[i][j + 1] == 1:
                        k = 2
                        # i, j = i + di[k], j + dj[k]
                    else:
                        k = 0
                        # i, j = i + di[k], j + dj[k]

            elif k != 0:
                if arr[i-1][j] == 1:
                    k = 0
                    # i, j = i + di[k], j + dj[k]
                else:
                    pass
                    # i, j = i + di[k], j + dj[k]
            i, j = i + di[k], j + dj[k]
            # print(i, j)


    print('#{0} {1}'.format(test_case, j))
