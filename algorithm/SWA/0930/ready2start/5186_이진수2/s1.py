import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    # bin_str: N의 이진수
    bin_str = "0."

    i = 1
    while N and i < 13:
        if (2 ** -i) <= N:
            N -= (2 ** -i)
            bin_str += '1'
        else:
            bin_str += '0'

        i += 1

    if N:
        print("#{} {}".format(tc, 'overflow'))
    else:
        print("#{} {}".format(tc, bin_str[2:]))
