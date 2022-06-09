import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    lst_90 = [[0] * N for _ in range(N)]
    lst_180 = [[0] * N for _ in range(N)]
    lst_270 = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            lst_270[N - 1 - c][r] = lst_180[N - 1 - r][N - 1 - c] = lst_90[c][N - 1 - r] = lst[r][c]

    print('#%s' %tc)
    for j in range(N):
        print(''.join(map(str, lst_90[j])), ''.join(map(str, lst_180[j])), ''.join(map(str, lst_270[j])))