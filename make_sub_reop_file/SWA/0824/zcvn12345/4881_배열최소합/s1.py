import sys
sys.stdin = open('input.txt')

def f(i, N, P):
    global result

    if i == N:
        temp = []
        for x in range(N):
            temp.append(mat[x][P[x]])
        if sum(temp) < result:
            result = sum(temp)


    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N, P)
            P[i], P[j] = P[j], P[i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    result = 2**30
    f(0, N, P)
    print(f'#{tc} {result}')


