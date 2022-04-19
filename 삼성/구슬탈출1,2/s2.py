import sys
sys.stdin = open("test.txt")
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    q = []
    visited = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == "R":
                ri, rj = i, j
            if arr[i][j] == "B":
                bi, bj = i, j
    q.append([ri, rj, bi, bj, 0])
    visited.append([ri, rj, bi, bj])

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    def go(i, j, x, y):
        ni, nj = i, j
        cnt = 0
        while True:
            cnt += 1
            ni += x
            nj += y
            if arr[ni][nj] == "O":
                break
            elif arr[ni][nj] == "#":
                ni -= x
                nj -= y
                break
        return ni, nj, cnt
    def bfs():
        while q:
            ri, rj, bi, bj, answer = q.pop(0)
            if answer > 10:
                print(-1)
                return

            if arr[ri][rj] == 'O' and arr[bi][bj] != "O":
                print(answer)
                return

            for i in range(4):
                nri, nrj, rcnt = go(ri, rj, di[i], dj[i])
                nbi, nbj, bcnt = go(bi, bj, di[i], dj[i])

                if arr[nbi][nbj] == 'O':
                    continue

                if nri == nbi and nrj == nbj:
                    if rcnt < bcnt:
                        nbi -= di[i]
                        nbj -= dj[i]
                    else:
                        nri -= di[i]
                        nrj -= dj[i]

                if [nri, nrj, nbi, nbj] not in visited:
                    q.append([nri, nrj, nbi, nbj, answer+1])
                    visited.append([nri, nrj, nbi, nbj])
        print(-1)
    bfs()
