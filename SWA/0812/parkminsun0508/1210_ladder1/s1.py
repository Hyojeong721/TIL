# 1210 ladder
# 강의 시간 코드 공유 후 참고

import sys
sys.stdin = open("input.txt")

# 방향 설정
# 1) 오른쪽 : d: 1 -> 0
# 2) 왼쪽 : d: 2 -> 0
# 3) 위 : 왼쪽이나 오른쪽 1 나오면 방향 바꾼다.

# 방향 설정 (위, 오른쪽, 왼쪽)
dr = [-1, 0, 0]
dc = [0, 1, -1]

# 10 개의 테스트 케이스가 주어진다.
T = 10
for tc in range(1, T+1):
    t = int(input())
    # padding 활용 양 끝에 벽을 세워주기 위해 0 칼럼 추가
    p = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # 도착점의 칼럼 인덱스 구하기
    for j in range(102):
        if p[99][j] == 2:
            c = j
    # 방향 0: 위 1: 오 2: 왼
    d = 0
    r = 99
    while True:
        if r == 0:
            break
        if p[r][c-1]:
            d = 2
            while True:
                r += dr[d]
                c += dc[d]
                if p[r][c-1] == 0:
                    break
        elif p[r][c+1]:
            d = 1
            while True:
                r += dr[d]
                c += dc[d]
                if p[r][c+1] == 0:
                    break
        d = 0
        r += dr[d]
        c += dc[d]
    print("#{} {}".format(t, c - 1))








