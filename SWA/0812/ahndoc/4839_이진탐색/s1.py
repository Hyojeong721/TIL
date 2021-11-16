import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    P, Pa, Pb = list(map(int, input().split()))

    a_l = 1
    a_r = P
    a_c = int((a_l + a_r) / 2)
    b_l = 1
    b_r = P
    b_c = int((b_l + b_r) / 2)
    count_a = 0
    count_b = 0

    while a_c != Pa:

        if a_c < Pa:
            count_a += 1
            a_l = a_c
            a_c = int((a_l + a_r) / 2)

        elif a_c > Pa:
            count_a += 1
            a_r = a_c
            a_c = int((a_l + a_r) / 2)
        else:
            count_a += 1
            break

    while b_c != Pb:

        if b_c < Pb:
            count_b += 1
            b_l = b_c
            b_c = int((b_l + b_r) / 2)

        elif b_c > Pb:
            count_b += 1
            b_r = b_c
            b_c = int((b_l + b_r) / 2)
        else:
            count_b += 1
            break

    if count_a < count_b:
        print('#{} A'.format(test_case))
    elif count_a > count_b:
        print('#{} B'.format(test_case))
    else:
        print('#{} 0'.format(test_case))