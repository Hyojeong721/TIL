import sys
sys.stdin = open('input.txt')

def get_purple(coloring_info):
    red = [[0] * 10 for _ in range(10)]
    blue = [[0] * 10 for _ in range(10)]
    purple = [[0] * 10 for _ in range(10)]
    for coloring in coloring_info:
        r1 = coloring[0]
        c1 = coloring[1]
        r2 = coloring[2]
        c2 = coloring[3]
        for i in range(c1, c2 + 1):
            for j in range(r1, r2 + 1):
                if coloring[-1] == 1:
                    red[i][j] = 1
                else:
                    blue[i][j] = 1
    for i in range(len(red)):
        for j in range(len(red[i])):
            if red[i][j] == 1 and blue[i][j] == 1:
                purple[i][j] = 1
    total = 0
    for row in purple:
        total += sum(row)

    return total


T = int(input())
for tc in range(1, T + 1):
    coloring_count = int(input())
    coloring_info = []
    for _ in range(coloring_count):
        coloring_info.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, get_purple(coloring_info)))