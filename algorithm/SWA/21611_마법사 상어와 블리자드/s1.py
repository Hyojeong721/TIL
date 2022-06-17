import sys
sys.stdin = open("input.txt")

def init():
    # (0,0) -> (N//2, N//2)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    num = N**2-1
    dist = N
    loc = (0, -1)
    dir = 0
    cnt = 1
    while True:
        for i in range(dist):
            ni, nj = loc[0]+dx[dir], loc[1]+dy[dir]
            loc = (ni, nj)
            LtoN[loc] = num
            NtoL[num] = loc
            NtoB[num] = arr[ni][nj]
            num -= 1
        cnt += 1
        dir = (dir+1) % 4
        if cnt == 2:
            cnt = 0
            dist -= 1

        if num == 0:
            LtoN[(N//2, N//2)] = num
            break

def spell(idx):
    dir, cnt = spells[idx]
    # dir = 1,2,3,4 = 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    return

def move():
    return

def bomb():
    return

def change():
    return

# idx = 마법 인덱스
def process(idx):
    # 구슬 파괴
    spell(idx)
    # 이동
    move()
    # 폭발
    bomb()
    # 구슬 변화
    change()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
spells = [list(map(int, input().split())) for _ in range(M)]


res = 0
LtoN = {}  # 좌표 -> 번호
NtoL = {}  # 번호 -> 좌표
NtoB = [-1] * (N * N)  # 번호에 해당하는 구슬번호

init()
for i in range(M):
    process(i)

print(res)