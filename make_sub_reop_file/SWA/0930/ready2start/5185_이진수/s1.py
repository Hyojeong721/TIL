import sys
sys.stdin = open('input.txt')


def hex_to_bin(hex_num):
    """
    N자리의 16진수 수의 각 자리 수를 4자리의 2진수 수(ex. '0011')로 변환한다.
    (ex. '1A3' => '000110100011')
    """
    total = ""

    for num in hex_num:
        # 16진수 => 10진수
        dec_num = int(num, 16)
        # 10진수 => 4자리 2진수
        total += bin(dec_num)[2:].zfill(4)

    return total


T = int(input())

for tc in range(1, T + 1):
    N, hex_num = input().split()

    print("#{} {}".format(tc, hex_to_bin(hex_num)))