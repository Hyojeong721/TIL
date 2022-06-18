# SWEA에서는 16진수 수들을 받을 때 rstrip()을 적용해야 런타임 에러가 나지 않음.

import sys
sys.stdin = open('input.txt')


hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

cipher_pattern = {
    '211': '0', '221': '1',
    '122': '2', '411': '3',
    '132': '4', '231': '5',
    '114': '6', '312': '7',
    '213': '8', '112': '9',
}


def check_code(t):
    """
    8자리 코드가 유효한 코드인지 검사한다.
      - 유효성 기준: (홀수 자리 수의 합) * 3 + (짝수 자리 수의 합)이 10의 배수
    """
    total = 0

    for i in range(8):
        if i % 2 == 0:
            total += (3 * int(t[i]))
        else:
            total += int(t[i])

    return total % 10 == 0


T = int(input())

for C in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    codes = set()

    for _ in range(N):
        board.append(input().rstrip())

    # 중복되는 열 제거하기
    board = list(set(board))

    # 문자열 리스트화하기
    for i in range(len(board)):
        board[i] = list(board[i])

    # 16진수를 2진수로 바꾸고 다시 문자열로 합치기
    for sub_board in board:
        if not sub_board:
            continue

        bin_num = ''.join([hex_to_bin[x] for x in sub_board])
        i = len(bin_num) - 1
        code = ""

        while i > 2:
            if bin_num[i] == '1':
                # 패턴의 길이를 잰다.
                # 각각 0/1/0/1에서 1/0/1의 개수
                second, third, fourth = 0, 0, 0
                while bin_num[i] == '1':
                    i -= 1
                    fourth += 1

                while bin_num[i] == '0':
                    i -= 1
                    third += 1

                while bin_num[i] == '1':
                    i -= 1
                    second += 1

                min_value = min(second, third, fourth)
                if min_value > 1:
                    second //= min_value
                    third //= min_value
                    fourth //= min_value

                pattern = str(second) + str(third) + str(fourth)
                code = cipher_pattern[pattern] + code

                if len(code) == 8:
                    codes.add(code)
                    code = ""
            else:
                i -= 1

    total = 0

    for code in codes:
        if check_code(code):
            total += sum([int(x) for x in code])

    print("#{} {}".format(C, total))

