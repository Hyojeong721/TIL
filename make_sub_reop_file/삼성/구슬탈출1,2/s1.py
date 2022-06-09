# from collections import deque
import sys
sys.stdin = open("test.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    q = []
    visited = []
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    def init():
        ri, rj, bi, bj = 0, 0, 0, 0
        for idx in range(N):
            for jdx in range(M):
                if arr[idx][jdx] == 'R':
                    ri, rj = idx, jdx
                if arr[idx][jdx] == "B":
                    bi, bj = idx, jdx
        q.append([ri, rj, bi, bj, 0])
        visited.append([ri, rj, bi, bj])



    def bfs():
        init()
        while q:
            ri, rj, bi, bj, answer = q.pop(0)
            if answer > 10:
                print(-1)
                return

            # 빨간공이 출구일때
            if arr[ri][rj] == 'O' and arr[bi][bj] != 'O':
                print(answer)
                return

            for i in range(4):
                rcnt, bcnt = 0, 0
                nri, nrj, nbi, nbj = ri, rj, bi, bj
                # 기울여서 갈수 있는데까지 일단 가
                while True:
                    nri, nrj = nri + di[i], nrj + dj[i]
                    rcnt += 1
                    if arr[nri][nrj] == '#':
                        nri -= di[i]
                        nrj -= dj[i]
                        break
                    elif arr[nri][nrj] == 'O':
                        break

                while True:
                    nbi, nbj = nbi + di[i], nbj + dj[i]
                    bcnt += 1
                    if arr[nbi][nbj] == '#':
                        nbi -= di[i]
                        nbj -= dj[i]
                        break
                    elif arr[nbi][nbj] == 'O':
                        break

                # 파란공이 출구일 때
                if arr[nbi][nbj] == 'O':

                    continue

                # 둘이 같은 자리일 때
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


