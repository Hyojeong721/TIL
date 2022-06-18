import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst_red = [[0] * 10 for _ in range(10)]
    lst_blue = [[0] * 10 for _ in range(10)]
    cnt = 0
    for n in range(N):
        lst = list(map(int, input().split()))

        if lst[-1] == 1: # red 영역 행렬 구성
            for i in range(lst[0], lst[2] + 1):
                for j in range(lst[1], lst[3] + 1):
                    lst_red[i][j] = 1
        else: # blue 영역 행렬 구성
            for i in range(lst[0], lst[2] + 1):
                for j in range(lst[1], lst[3] + 1):
                    lst_blue[i][j] = 1

    for r in range(10):
        for c in range(10):
            if lst_red[r][c] == 1 and lst_blue[r][c] == 1:
                cnt += 1

    print('#{} {}'.format(tc, cnt))