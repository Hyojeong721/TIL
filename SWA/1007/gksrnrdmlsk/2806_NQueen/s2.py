import sys
sys.stdin = open('input.txt')

def counting(curr):
    global answer
    if curr == N:
        answer += 1
    else:
        for i in range(N):
            if visited[i] == 0:
                state = 1
                for idx, value in enumerate(whole[:curr]):
                    if value - (curr - idx) == i or value + (curr - idx) == i:
                        state = 0
                if state:
                    visited[i], whole[curr] = 1, i
                    counting(curr + 1)
                    visited[i], whole[curr] = 0, -1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * N # 각 열을 방문하였는지 저장
    whole = [-1] * N # 각 행에서 무엇을 선택하였는지 저장
    answer = 0
    counting(0)
    print('#{} {}'.format(tc, answer))

