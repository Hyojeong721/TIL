import sys
sys.stdin = open('input.txt')


T = int(input())

for TC in range(1, T+1):
    answer = ''
    # N * N 크기
    # M : 회문의 길이
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    for n in range(N):
        arr[n] = input()

    # 가로 방향
    for i in range(N):
        for j in range(N-M+1):
            cir_str = ''
            for m in range(M):
               cir_str += arr[i][j+m]
            k = 0
            l = 0
            while k < int(M/2):
                if cir_str[k] != cir_str[M-1-l]:
                    break
                if k == int(M/2)-1:
                    answer = cir_str
                k += 1
                l += 1

    # 세로 방향
    for j in range(N):
        for i in range(N-M+1):
            cir_str = ''
            for m in range(M):
               cir_str += arr[i+m][j]
            k = 0
            l = 0
            while k < int(M/2):
                if cir_str[k] != cir_str[M-1-l]:
                    break
                if k == int(M/2)-1:
                    answer = cir_str
                k += 1
                l += 1
    print('#{} {}'.format(TC, answer))