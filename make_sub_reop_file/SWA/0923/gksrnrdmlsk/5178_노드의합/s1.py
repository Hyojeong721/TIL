import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = [0] * (N + 1)
    
    # 리프노드 값들 받아오기
    for i in range(M):
        idx, value = map(int, input().split())
        lst[idx] = value
    
    # 자식노드 합 구하기    
    for i in range(N - M, 0, -1):
        total = lst[i]
        if 2 * i <= N:
            total += lst[2 * i]
        if 2 * i + 1 <= N:
            total += lst[2 * i + 1]
        lst[i] = total

    print('#{} {}'.format(tc, lst[L]))