# 재귀로
import sys
sys.stdin = open('input.txt')

def rec_magn(row, curr): # 기본적으로 1 다음에 나오는 2에만 관심있는 재귀함수
    global cnt
    while curr < 100:
        if lst[row][curr] != 1:
            curr += 1
            pass

        else: # 1이 나왔다면, 2를 탐색!
            for i in range(curr, N):
                if lst[row][i] == 2:
                    cnt += 1
                    rec_magn(row, i + 1) # 2를 찾았다면 그 다음부터 처음처럼 1을 탐색.
                    return
            return # 2가 안 나온다면 그대로 끝

T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N): # 세로로 코드 짜기 어렵고 헷갈려서 전치행렬 생성
        for c in range(N):
            if r > c:
                lst[r][c], lst[c][r] = lst[c][r], lst[r][c]

    cnt = 0 # 우리가 관심있어 하는 교착상태의 수
    for i in range(N): # 각 행별로(원래대로라면 열별로) 교착상태 개수 탐색
        rec_magn(i, 0)

    print('#{} {}'.format(tc, cnt))

