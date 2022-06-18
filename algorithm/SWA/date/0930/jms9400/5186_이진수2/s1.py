import sys
sys.stdin = open('input.txt')

T = int(input())


def Bbit_print(num):
    output = ""

    for i in range(-1, -14, -1):
        if num == 0:
            return output
        if 2 ** i <= num:
            output += '1'
            num -= (2 ** i)
        else:
            output += '0'
    return 'overflow'


for tc in range(1, T + 1):
    N = float(input())
    print('#{} {}'.format(tc, Bbit_print(N)))