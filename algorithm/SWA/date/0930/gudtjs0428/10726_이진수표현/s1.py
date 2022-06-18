import sys
sys.stdin = open('input.txt')

def if_all_1(N, M):
    bina = ''
    while M:
        if M % 2:
            bina = '1' + bina
        else:
            bina = '0' + bina
        M //= 2

    if N > len(bina):
        return 'OFF'
    if bina[:-N-1:-1] == '1' * N:
        return 'ON'
    return 'OFF'


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    print('#{} {}'.format(test_case, if_all_1(N, M)))