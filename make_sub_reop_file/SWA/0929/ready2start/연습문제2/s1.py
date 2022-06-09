import sys
sys.stdin = open('input.txt')


def hex_to_bin(hex_num):
    """
    1자리 16진수 수를 4자리의 2진수 수로 변환한다.
    (ex. '6' => '0110', 'C' => '1100')
    """
    # 1. 16진수 => 10진수
    dec = int(hex_num, 16)
    # 2. 10진수 => 2진수 (앞의 '0b'를 없애고, 4자리로 만들어준다.)
    bin_num = bin(dec)[2:].zfill(4)
    return bin_num


# 연습문제 1의 함수 재활용
def bin_to_dec(bin_num):
    """
    문자열로 주어지는 2진수 수를 10진수 수로 바꾼다.
    """
    total = 0

    for i, num in enumerate(bin_num[::-1]):
        # 현재 탐색 중인 숫자가 1이면 2 ** i를 더한다.
        if num == '1':
            total += 2 ** i

    return total


input_number = input()
full_string = ""

for num in input_number:
    full_string += hex_to_bin(num)

for i in range(0, len(full_string), 7):
    print(bin_to_dec(full_string[i:i + 7]), end=" ")
