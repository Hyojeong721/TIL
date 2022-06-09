# 교수님의 풀이

import sys
sys.stdin = open('input.txt')

def permutation(k, cursum):
    global visited, result
    # 가지치기 : 현재 합이 result보다 크다면 더 이상 더할 가치가 없음
    if result <= cursum:
        return

    # 전체를 다 바꾼 경우 => 순열이 하나 생성
    if k == N:
        if cursum < result:
            result = cursum

    for idx in range(k, N):
        visited[k], visited[idx] = visited[idx], visited[k]
        permutation(k+1, cursum + data[k][visited[k]])
        visited[k], visited[idx] = visited[idx], visited[k]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())

    visited = [0] * N
    for i in range(N):
        visited[i] = i

    data = [list(map(int, input().split())) for _ in range(N)]
    result = 1000

    permutation(0, 0)
    print(result)