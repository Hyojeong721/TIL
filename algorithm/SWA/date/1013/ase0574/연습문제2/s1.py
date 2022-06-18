import sys
sys.stdin = open('input.txt')

# 모든 정점을 너비 우선 탐색하여 화면에 너비우선탐색경로 출력
# 시작정점 1
# 결과 -> 1-2-3-4-5-7-6


arr = list(map(int, input().split()))
q = []
visited = [0] * len(arr)

def bfs(v):
    q.append(v)
    visited[v] = 1

    while q:
        v = q.pop(0)
        print(v, end='-')
        for i in range(len(arr)//2):
            if arr[i*2] == v:
                u = arr[2*i+1]
                if visited[u] == 0:
                    q.append(u)
                    visited[u] = visited[v]+1
bfs(1)