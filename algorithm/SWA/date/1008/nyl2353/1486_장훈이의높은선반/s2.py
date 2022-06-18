'''
    망코드 ㅎㅎ
        text case 8부터 급격하게 오래 걸린다. (N이 15 이상)
'''
import sys
sys.stdin = open('input.txt')


def find_minsum(H_sum):
    global H_min, visited

    if H_sum < B:
        return
    if H_sum == B:
        H_min = B
        return
    if H_sum < H_min:
        H_min = H_sum

    for idx in range(N):
        if visited[idx]:
            visited[idx] = False
            find_minsum(H_sum - H[idx])
            visited[idx] = True


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    H_total = sum(H)
    H_min = H_total
    visited = [True] * N
    find_minsum(H_total)

    print('#{} {}'.format(tc, H_min - B))
