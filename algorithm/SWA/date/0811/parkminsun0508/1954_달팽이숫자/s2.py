# 달팽이 숫자 강의 중 풀이
N = int(input())
    dal_list = [[0]*N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 1
    i, j = 0, -1
    k = 0

    while cnt <= N*N:
        ni, nj = i+di[k], j+dj[k]

        if ni < N and nj < N and dal_list[ni][nj] == 0:
            dal_list[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k + 1) % 4

    print('#{}'.format(tc + 1))

    for row in range(len(dal_list)):
        for col in range(len(dal_list[row])):
            print(dal_list[row][col], end=" ")
        print()