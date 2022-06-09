import sys
sys.stdin = open('input.txt')

T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for tc in range(T):
    rows = int(input())
    lst = [list(map(int, input().split())) for row in range(rows)]
    result_lst = [[0] * rows for row in range(rows)]
    cnt = 0
    for i in range(rows):
        for j in range(rows):
            for k in range(4):
                if i + dx[k] >= 0 and j + dy[k] >= 0:
                    try:
                        cnt += abs(lst[i][j] - lst[i + dx[k]][j + dy[k]])
                    except:
                        pass
    print(cnt)