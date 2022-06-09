# 인접리스트로 풀기!

import sys
sys.stdin = open('input.txt')

def is_road(s, g):
    global graph
    stack = [s]
    visited = [0] * 100
    while stack:
        current = stack.pop()
        if visited[current] == 0:
            visited[current] = 1
            for i in graph[current]:
                if visited[i] == 0:
                    stack.append(i)
    if visited[g] == 1:
        return 1
    else:
        return 0


T = 10

for tc in range(1, T+1):
    tc, edges = map(int, input().split())
    # 인접리스트 만들기
    graph = [[] * 100 for _ in range(100)]
    numbers = list(map(int, input().split()))

    for idx, value in enumerate(numbers):
        if idx % 2: # 순서쌍을 통해서 인접리스트를 완성합니다.
            graph[numbers[idx - 1]].append(value)



    print('#{} {}'.format(tc, is_road(0, 99)))
