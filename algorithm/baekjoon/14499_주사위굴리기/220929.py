import sys
sys.stdin = open('input.txt')
# 지도 0 -> 주사위 바닥면이 지도에 복붙
# 그렇지 않은 경우 -> 칸에있는 수가 주사위 바닥면으로 복붙 + 칸은 0
di, dj = [0, 0, -1, 1], [1, -1, 0, 0]
def change(k):
    global ran
    if k == 1:
        temp1, temp2 = ran[0], ran[1]
        ran[0], ran[1] = ran[3], ran[2]
        ran[2], ran[3] = temp1, temp2
    elif k == 2:
        temp1, temp2 = ran[0], ran[1]
        ran[0], ran[1] = ran[2], ran[3]
        ran[3], ran[2] = temp1, temp2
    elif k == 3:
        temp1, temp2 = ran[0], ran[1]
        ran[0], ran[1] = ran[4], ran[5]
        ran[5], ran[4] = temp1, temp2
    elif k == 4:
        temp1, temp2 = ran[0], ran[1]
        ran[0], ran[1] = ran[5], ran[4]
        ran[4], ran[5] = temp1, temp2

def is_range(i, j):
    if 0<=i<N and 0<=j<M:
        return True
    return False

def process(t):
    global ran, i, j, arr

    # 새로운 자리로 이동
    ni, nj = i+di[t], j+dj[t]

    # 범위체크
    if not is_range(ni, nj):
        return False
    i, j = ni, nj

    # 주사위 이동
    change(t+1)

    # 이동한 자리 조건맞춰 숫자 변경
    if arr[i][j] == 0:
        arr[i][j] = ran[1]
    else:
        ran[1] = arr[i][j]
        arr[i][j] = 0

    return True

N, M, i, j, K  = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
pos = list(map(int, input().split()))
ran = [0, 0, 0, 0, 0, 0]


for k in range(K):
    if process(pos[k]-1):
        print(ran[0])
