'''
    LIVE - check
        53,448 kb / 143 ms / 855 lines

    LIVE - check2
        55,540 kb / 160 ms / 1,024 lines
'''

import sys
sys.stdin = open('input.txt')


def change_to_dec(num, notation):
    tmp = 0

    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val * (notation**n)
    return tmp

def check(num, notation):
    change_num = change_to_dec(num, notation)
    # change_num = int(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):
            if val == j: continue
            tmp = change_num - val * notation**n + j * notation**n

            # 2진수 차곡차곡 저장, 3진수도 저장하다가 똑같은 수 발견하면 else ㄱㄱ!
            if tmp not in binary:
                binary.append(tmp)
            # else: 3진수 위함
            else:
                return tmp


def check2():
    # 2진수 문자열 10진수로 변환
    bi_num = 0
    for x in bi:
        bi_num = bi_num*2 + int(x)

    # 2진수 후보들 생성
    for i in range(len(bi)):
        # exclusive OR : ^
        # => 한글자씩 바꿈 (0은 1로, 1은 0으로)
        binary.append(bi_num ^ (1 << i))

    # 3진수 후보 생성하며 10진수로 변환
    # i번째 자리 바꿀거임
    for i in range(len(tr)):
        num1 = 0
        num2 = 0
        # i = j 인 경우만 숫자 바꾸고, 아닌 경우는 원래 값으로 계산
        for j in range(len(tr)):
            if i != j:
                num1 = num1 * 3 + int(tr[j])
                num2 = num2 * 3 + int(tr[j])
            else:
                num1 = num1 * 3 + (int(tr[j]) + 1) % 3
                num2 = num2 * 3 + (int(tr[j]) + 2) % 3

            if num1 in binary:
                return num1
            if num2 in binary:
                return num2


T = int(input())
for tc in range(1, T + 1):
    bi = list(input())
    tr = list(input())

    binary = []

    # check(bi, 2)
    # print('#{} {}'.format(tc, check(tr, 3)))

    print('#{} {}'.format(tc, check2()))
