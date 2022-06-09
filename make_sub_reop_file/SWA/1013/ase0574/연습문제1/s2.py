#두개의 정점 사이의 간선을 순서대로 나열한 것
# 모든 정점을 깊이우선탐색하여 화면에
# 깊이 우선 탐색 경로를 출력하시오
# 시작 정점 1

# 예상 결과 -> 1-2-4-6-5-7-3 / 1-3-7-6-5-2-4

import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))
visited = [0] * len(arr)

s = []

def dfs(v):
    s.append(v)
    visited[v] = 1

    while s:
        v = s.pop()
        if visited[v] == 0:
            visited[v] = 1
            print(v, end='-')

        for i in range(len(arr)//2):
            if arr[2*i] == v and visited[arr[2*i+1]] == 0:
                s.append(arr[2*i+1])

            if arr[2 * i + 1] == v and visited[arr[2 * i]] == 0:
                s.append(arr[2 * i])

dfs(1)

