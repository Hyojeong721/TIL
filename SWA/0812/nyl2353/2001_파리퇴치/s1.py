import sys
sys.stdin = open('input.txt')

def remove_max_fly(mat, N, M):
    """
    한번에 최대 파리를 잡았을 때 마리 수를 반환하는 함수
    mat: 파리가 있는 격자
    N: 격자의 한 면 길이
    M: 파리채의 한 면 길이

    """
    max_sum = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            temp_sum = 0
            for tr in range(r, r + M):
                for tc in range(c, c + M):
                    temp_sum += mat[tr][tc]
            if temp_sum > max_sum:
                max_sum = temp_sum

    return max_sum

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    mat = []
    for i in range(N):
        mat.append(list(map(int, input().split())))
    fly_num = remove_max_fly(mat, N, M)
    print('#{0} {1}'.format(tc, fly_num))