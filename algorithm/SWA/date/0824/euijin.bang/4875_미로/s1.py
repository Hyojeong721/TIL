import sys
sys.stdin = open("input.txt")

# DFS 미로는 백트래킹아님..
# 도착지에 갈때까지 10이하여야한다.. -> 10 넘으면 쳐낸다 -> 이것이 플러닝 !


def is_there_Route(i,j , arr):
    """
    i,j : 시작위치 좌표

    :return: 출발지에서 목적지까지 도착 경로가 존재하면 1(True), 아니면 0(False)를 출력

    # N: 미로의 크기 N * N 배열
    # 0: 통로, 1: 벽, 2: 출발지, 3: 도착지

    PATH_TOKEN = "X"
    TRIED_TOKEN = "o"
    """

    # 델타탐색 초기값 설정한다. 방향은 상-하-좌-우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    stack = []

    # 시작점에 stack 찍고 시작
    if len(stack) == 0 and arr[i][j] == 2:
        stack.append("X")

    # 스택이 남아있는 동안 동작을 수행한다.
    while len(stack) != 0:
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 길이 있다면 스택 X 쌓으며 전진한다.
                if arr[ni][nj] == 0:
                    stack.append("X")
                    i, j = ni, nj
                    if arr[i][j] == 3:
                        return 1
            # 길이 없다면(벽을 만난다면) 스택 X 치우고 스택 o 쌓고 돌아간다.
            else:
                    stack.pop()
    # 스택이 없다 => 길이 없다
    return 0


T = int(input())

for tc in range(1, T+1):
    # 배열 크기
    N = int(input())

    # 미로 N * N 배열을 초기화한다.
    arr = [list(map(int, input())) for _ in range(N)]

    # 시작위치 설정
    val = 2
    for idx, row in enumerate(arr):
        print(idx, row)
        if val in row:
            i,j = idx, row.index(val)

    print("#{} {}".format(tc, is_there_Route(i, j, arr)))