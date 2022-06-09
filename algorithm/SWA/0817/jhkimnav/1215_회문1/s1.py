import sys
sys.stdin = open('input.txt')

T = 10

for TC in range(1, T+1):
    answer = 0
    M = int(input())
    arr = [[0] for _ in range(8)]

    for n in range(8):
        arr[n] = input()

    # 가로 방향
    for i in range(8):
        for j in range(8-M+1):
            cir_str = ''
            for m in range(M):
               cir_str += arr[i][j+m]

            for k in range(M//2):
                if cir_str[k] != cir_str[-1-k]:
                    break
                if k == (M // 2) - 1:
                    answer += 1
    # 세로 방향
    for j in range(8):
        for i in range(8-M+1):
            cir_str = ''
            for m in range(M):
               cir_str += arr[i+m][j]

            for k in range(M//2):
                if cir_str[k] != cir_str[-1-k]:
                    break
                if k == (M // 2) - 1:
                    answer += 1

    print('#{} {}'.format(TC, answer))