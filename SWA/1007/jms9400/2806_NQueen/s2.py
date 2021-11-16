import sys
sys.stdin = open('input.txt')

T = int(input())

def queen(i):
    global answer

    if i == N:
        answer += 1
        return

    for k in range(N):
        if promising(i, k):
            arr[i][k] = 1
            queen(i+1)
            arr[i][k] = 0

def promising(i, k):
    temp = k
    temp2 = k
    for x in range(i-1, -1, -1):   # 위, 좌대각선, 우대각선 괜찮으면 1반환
        if arr[x][k] == 1:  # 위
            return 0
        if temp >= 1 and arr[x][temp-1] == 1:  # 좌대각선
            return 0
        if temp2 + 1 < N and arr[x][temp2+1] == 1:  # 우대각선
            return 0
        temp -= 1
        temp2 += 1
    return 1


for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    answer = 0

    queen(0)
    print('#{} {}'.format(tc, answer))