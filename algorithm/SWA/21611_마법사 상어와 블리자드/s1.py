import sys
sys.stdin = open("input.txt")

def init():
    num = N**2 -1
    dist = N
    loc = (0, -1)
    cnt = 1
    dir = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while True:

        for i in range(dist):
            ni, nj = loc[0]+di[dir], loc[1]+dj[dir]
            loc = (ni, nj)
            LtoN[loc] = num
            NtoL[num] = loc
            NtoB[num] = arr[ni][nj]
            num -= 1
        cnt += 1
        dir = (dir+1)%4
        if cnt == 2:
            cnt = 0
            dist -= 1
        if num == 0:
            break


def is_range(i, j):
    if 0<= i < N and 0 <= j <N:
        return True
    return False

def spell(idx):
    dir, cnt = spells[idx]
    di = ["", -1, 1, 0, 0]
    dj = ["", 0, 0, -1, 1]
    while cnt != 0:
        ni, nj = N // 2 + (di[dir]*cnt), N // 2 + (dj[dir]*cnt)
        num = LtoN[(ni, nj)]
        NtoB[num] = 0
        cnt -= 1
    return

def move():
    new = [-1] * N * N
    idx = 0
    # 자리 이동 (땅기기)
    for i in range(N*N):
        if NtoB[i] == 0:
            continue
        else:
            new[idx] = NtoB[i]
            idx += 1
    # 뒤에 남은 빈칸 채우기
    for i in range(idx, N*N):
        new[i] = 0
    # 복사하기
    for i in range(N*N):
        NtoB[i] = new[i]
    return


def search_bomb():
    global res
    msg = False
    idx, cnt = 0, 1
    for i in range(1, N*N):
        if NtoB[idx] != NtoB[i]:
            if cnt >= 4:
                msg = True
                res += cnt*NtoB[idx]
                for c in range(cnt):
                    NtoB[idx] = 0
                    idx += 1
            cnt = 1
            idx = i
        else:
            cnt += 1
    return msg

def change():
    new = [-1]
    idx, cnt = 1, 1
    for i in range(2, N*N):
        if NtoB[i] != NtoB[idx]:
            new.extend([cnt, NtoB[idx]])
            cnt = 1
            idx = i
        else:
            cnt += 1
    idx = len(new)
    # 복사
    for i in range(N*N):
        if i >= idx:
            NtoB[i] = 0
        else:
            NtoB[i] = new[i]
    return

# idx = 마법 인덱스
def process():
    init()
    for i in range(M):
        # 구슬 파괴
        spell(i)
        # 이동
        move()
        # 폭발 & 이동
        while search_bomb():
            move()
        # 구슬 변화
        change()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
spells = [list(map(int, input().split())) for _ in range(M)]


res = 0
LtoN = {}  # 좌표 -> 번호
NtoL = {}  # 번호 -> 좌표
NtoB = [-1] * (N * N)  # 번호에 해당하는 구슬번호

process()
print(res)