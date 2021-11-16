import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    result = 0

    visited = [0] * N
    trucks.sort(reverse=True)
    containers.sort(reverse=True)
    for i in range(M):
        for j in range(N):
            if trucks[i] >= containers[j] and not visited[j]:
                result += containers[j]
                visited[j] = 1
                break

    print('#{} {}'.format(tc, result))
