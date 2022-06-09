import sys
sys.stdin = open('input.txt')
# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램
T = 10

for tc in range(1, T+1):
    case_number = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    q = []
    visited = []

    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]

    # 시작점 (1,1) 끝점 (end_x, end_y)
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 3:
                end_x = i
                end_y = j

    q.append([1, 1])
    visited.append([1, 1])
    result = 0
    while q:
        point = q.pop(0)
        x = point[0]
        y = point[1]

        if maze[x][y] == 3:
            result = 1
            print("#{} 1".format(tc))

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < 16 and 0 <= new_y < 16:
                if [new_x, new_y] not in visited:
                    if maze[new_x][new_y] != 1:
                        q.append([new_x, new_y])
                        visited.append([new_x, new_y])
    if result == 0:
        print("#{} 0".format(tc))