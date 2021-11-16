import sys
sys.stdin = open('input.txt')

def f(k, temp_sum):
    """
    k번째에 이동할 관리구역을 고르고, 지금까지의 합에 k번째 이동의 배터리 사용량을 더해 최소값이 되는지 검사

    """
    global minsum

    # 관리실(1)로 돌아가는 배터리 사용량을 더해 현재까지의 최소합(minsum) 과 대소비교
    if k == N:
        temp = temp_sum + e[p[k-1]][1]
        if temp < minsum:
            minsum = temp
        return

    # k번째 이동에서 배터리사용량이 최소보다 적다면, k+1로 이동 (재귀)
    else:
        for i in range(k, N):
            p[k], p[i] = p[i], p[k]
            temp = temp_sum + e[p[k-1]][p[k]]
            if temp <= minsum:
                f(k+1, temp)
            p[k], p[i] = p[i], p[k]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    e = [[0 for _ in range(N+1)]]
    for _ in range(N):
        e.append([0]+list(map(int, input().split())))

    p = [i for i in range(1, N+1)]
    minsum = 100 * N * N
    f(1, 0)
    print('#{} {}'.format(tc, minsum))
