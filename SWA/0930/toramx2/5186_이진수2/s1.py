import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    num = float(input())
    i = 1
    num_2 = ''
    while num > 0:
        if ((1/2) ** i) <= num:
            num -= ((1/2) ** i)
            num_2 += '1'
        else:
            num_2 += '0'
        i += 1

    if len(num_2) >= 13:
        result = 'overflow'
    else:
        result = num_2

    print('#{} {}'.format(test_case, result))