import sys
sys.stdin = open('input.txt', 'r')


# idx = row, value = col
def is_compatible(i, arr):
    for j in range(i-1):
        for k in range(j+1, i):
            if abs(j-k) == abs(arr[j]-arr[k]):
                return 1
    return 0


def backtracking(i, arr):
    global possible
    # 대각선 체크
    if i >= 2:
        if is_compatible(i, arr):
            return
    # N개 모두 체스판 위에 올렸을 때
    if i == N:
        possible += 1
        return
    # 계속 경우의 수를 탐색하는 경우
    else:
        for j in range(N):
            if j not in arr:
                arr.append(j)
                backtracking(i+1, arr)
                arr.remove(j)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    locations = []
    possible = 0
    backtracking(0, locations)
    print(f'#{tc} {possible}')

