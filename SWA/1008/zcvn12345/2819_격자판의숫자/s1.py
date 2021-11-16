import sys
sys.stdin = open('input.txt')

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def search(i, num, x, y):
    global num_lst
    if i == 6:
        num_lst.append(num)
        return
    for w in range(4):
        tx = x + dx[w]
        ty = y + dy[w]
        if 0 <= tx < 4 and 0 <= ty < 4:
            search(i+1, num+mat[ty][tx], tx, ty)




for tc in range(1, T+1):
    mat = [list(input().split()) for _ in range(4)]
    cnt = 0
    num_lst = []
    for i in range(4):
        for j in range(4):
            search(0, mat[i][j], j, i)
    num_lst = list(set(num_lst))
    print(f'#{tc} {len(num_lst)}')