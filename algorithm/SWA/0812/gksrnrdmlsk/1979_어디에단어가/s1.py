import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for x in range(1, N):
        if lst[x - 1][0] == 0 and lst[x][0] == 1:
            cnt += 1

        if lst[0][x-1] == 0 and lst[0][x: x + K] == 1:
            cnt += 1

    for i in range(1, N):
        for j in range(1, N):
            if lst[i-1][j] == 0 and lst[i][j-1] == 0:
                try:
                    if sum(lst[i][:j+K]) == K and (j + K == N or lst[i][j+K] == 0):
                        print('첫 경우', i, j)
                        cnt += 1
                except:
                    pass


                try:
                    temp = 0
                    for number in range(i, i + K):
                        temp += lst[number][j]
                    if temp == K and (i+K == N or lst[i+K][j] == 0):
                        cnt += 1
                        print('temp:', temp, i, j)
                except:
                    pass

    print(cnt)