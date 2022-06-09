import sys
sys.stdin = open('input.txt')


def bfs(percent, i):   # i : 깊이=사람 (0부터 시작)
    global visited, max_value
    if percent <= max_value:   # 중간 확률이 최대 확률보다 이미 작아지면 더 이상 확인하지 않고 끝냄
        return
    if i == N:   # 모든 사람에게 일 분배가 완료된 경우
        if max_value <= percent:
            max_value = percent
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            bfs(percent*board[i][j], i+1)
            visited[j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())   # N명, N개의 일
    board = [list(map(lambda x: int(x)*0.01, input().split())) for _ in range(N)]

    visited = [0]*N
    max_value = 0

    bfs(1, 0)
    # result = format(max_value*100, '.6f')   # 소수점 6번째 자리까지 출력
    print('#{} {:.6f}'.format(tc, max_value*100))