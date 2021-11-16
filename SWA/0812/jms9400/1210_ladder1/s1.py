import sys
sys.stdin = open('input.txt')

def find_ladder(x, y):

    while x > 0:
        # 지나간 길 표시해주기 (왔던 길 되돌아가지 않도록)
        ladder[x][y] = 3
        # 우 확인
        if y+1 in range(0, 100) and ladder[x][y+1] == 1:
            y += 1
        # 좌 확인
        elif y-1 in range(0, 100) and ladder[x][y-1] == 1:
            y -= 1
        # 좌우 1이 없으면 위로
        else:
            x -= 1
    return y


for tc in range(1, 11):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[99][i] == 2:
            print('#{} {}'.format(n, find_ladder(99, i)))
            break

