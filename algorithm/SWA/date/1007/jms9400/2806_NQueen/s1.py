import sys
sys.stdin = open('input.txt')

T = int(input())

def queen(i):
    global answer

    if i == N:
        answer += 1
        return

    for k in range(N):
        c = 0
        if i >= 1:  # 위 확인
            temp = i
            while temp:
                if arr[temp - 1][k] == 1:
                    c = 1
                    break
                temp -= 1
        if c == 1:
            continue

        if i >= 1 and k >= 1:  # 좌 대각선 확인
            temp = i
            temp2 = k
            while temp and temp2:
                if arr[temp - 1][temp2 - 1] == 1:
                    c = 1
                    break
                temp -= 1
                temp2 -= 1
        if c == 1:
            continue

        if i >= 1 and k + 1 < N:  # 우 대각선 확인
            temp = i
            temp2 = k
            while temp != 0 and temp2 + 1 < N:
                if arr[temp - 1][temp2 + 1] == 1:
                    c = 1
                    break
                temp -= 1
                temp2 += 1
        if c == 1:
            continue

        arr[i][k] = 1
        queen(i+1)
        arr[i][k] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    answer = 0

    queen(0)
    print('#{} {}'.format(tc, answer))