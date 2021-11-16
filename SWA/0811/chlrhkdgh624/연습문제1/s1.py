import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for tc in range(1, T+1):
    rows = int(input())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    total = 0
    for i in range(rows):
        for j in range(len(matrix[0])):
            for k in range(4):
                delta_x = i + dx[k]
                delta_y = j + dy[k]
                if 0 <= delta_x < 5 and 0 <= delta_y < 5:
                    neighbour = matrix[delta_x][delta_y]
                    if neighbour > matrix[i][j]:
                        total += neighbour - matrix[i][j]
                    else:
                        total += matrix[i][j] - neighbour
    print(total)



