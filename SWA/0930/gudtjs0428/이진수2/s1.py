import sys
sys.stdin = open('input.txt')

def n_to_bin(num):
    bina = ''
    n = 0
    for i in range(1, 13):
        tmp = 2 ** -i
        if n + tmp > num:
            bina += '0'
        else:
            n += tmp
            bina += '1'
        if n == num:
            return bina
    return 'overflow'


T = int(input())
for test_case in range(1, T + 1):
    num = float(input())
    print('#{} {}'.format(test_case, n_to_bin(num)))