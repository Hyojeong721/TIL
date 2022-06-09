import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(1, T+1):
    answer = 0
    # M = int(input())
    TC = int(input())
    arr = [[0] for _ in range(100)]

    for n in range(100):
        arr[n] = input()

    palindrome = False
    M = 100
    # for M in range(100, 0, -1):

    while palindrome is False and M > 0:
        # 가로 방향
        i = 0
        while i < 100:
            for j in range(100-M+1):
                    cir_str = ''
                    for m in range(M):
                        cir_str += arr[i][j+m]

                    for k in range(M//2):
                        if cir_str[k] != cir_str[-1-k]:
                            break
                        if k == (M // 2) - 1:
                            if M > answer:
                                answer = M
                                palindrome = True
            i += 1
        M -= 1
    # 세로 방향
    palindrome = False
    M = 100
    while palindrome is False and M > 0:
        j = 0
        while j < 100:
            for i in range(100-M+1):
                cir_str = ''
                for m in range(M):
                   cir_str += arr[i+m][j]
                for k in range(M//2):
                    if cir_str[k] != cir_str[-1-k]:
                        break
                    if k == (M // 2) - 1:
                        if M > answer:
                            answer = M
                            palindrome = True
            j += 1
        M -= 1
    print('#{} {}'.format(TC, answer))