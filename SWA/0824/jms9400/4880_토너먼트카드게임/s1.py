import sys
sys.stdin = open('input.txt')

T = int(input())


def rsp_game(a, b):
    # 가위바위보 함수 길이 더 줄일 수 있음 (이기는 경우 / 지는 경우 나눠서)
    if arr[a] == arr[b]:
        return a
    if arr[a] == 1:  # 가위
        if arr[b] == 3:  # 보
            return a
        elif arr[b] == 2:  # 바위
            return b
    elif arr[a] == 2:
        if arr[b] == 1:
            return a
        elif arr[b] == 3:
            return b
    else:
        if arr[b] == 1:
            return b
        elif arr[b] == 2:
            return a


def dv_team(i, j):
    if i == j:
        return i
    elif i + 1 == j:
        return rsp_game(i, j)

    mid = (i+j) // 2
    s1 = dv_team(i, mid)
    s2 = dv_team(mid+1, j)
    return rsp_game(s1, s2)



for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print('#{} {}'.format(tc, dv_team(0, N-1)+1))
