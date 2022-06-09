import sys
sys.stdin = open('input.txt')


def binary_to_decimal(bin_num):
    """
    2진수 수를 10진수 수로 바꾼다.
    Args:
        bin_num: 2진수 수 (문자열)
    """
    total = 0

    for i, num in enumerate(bin_num[::-1]):
        # 현재 탐색 중인 숫자가 1이면 2 ** i를 더한다.
        if num == '1':
            total += 2 ** i

    return total


bin_num = input()
for i in range(0, len(bin_num), 7):
    # 7자리씩 끊어서 10진수 수로 변환시킨다.
    dec_num = binary_to_decimal(bin_num[i:i + 7])
    print(dec_num, end=" ")
