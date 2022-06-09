# 1210 ladder 유튜브 라이브 교수님이 해주신 풀이

import sys
sys.stdin = open("input.txt")

#도착지에서 위로 올라가는 함수
def search(start):
    i = 99
    j = start
    # 맨 윗줄에 도착하기 전까지 위로 올라감
    while i > 0:
        # 위로 한 칸 이동
        i -= 1
        # 왼쪽 칸이 1이면
        if j > 0 and ladder[i][j-1] == 1:
            # 사다리를 벗어나거나 0일때까지 왼쪽이동
            while j > 0 and ladder[i][j-1] ==1:
                j -= 1
        elif j < 99 and ladder[i][j+1] == 1:
            while j < 99 and ladder[i][j+1] == 1:
                j += 1
        # 0번 행에 도착했을 때의 열 리턴
        return j


# 10 개의 테스트 케이스가 주어진다.
T = 10
for tc in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착지 검색
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)
    print('#{} {}'.format(tc,ans))


