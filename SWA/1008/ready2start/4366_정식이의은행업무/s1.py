import sys
sys.stdin = open('input.txt')


def get_answer(binary, ternary):
    """
    2진수 binary와 3진수 ternary가 주어질 때,
    두 수에서 각각 숫자 하나를 바꾸어 만들 수 있는 수를 구한다.
    """
    # b_num, t_num: 2진수 / 3진수 수의 10진수 정수값
    b_num, t_num = int(binary, 2), int(ternary, 3)
    B, T = len(binary), len(ternary)

    # candidates: 2진수 수에서 숫자 하나를 바꾸어 만들 수 있는 수의 모음
    candidates = set()

    for i in range(len(binary) - 1, -1, -1):
        if binary[B - 1 - i] == '0':
            candidates.add(b_num + 2 ** i)
        else:
            candidates.add(b_num - 2 ** i)

    """
    3진수에서 각각 2, 1, -1, -2를 더하는 경우를 탐색한다.
      - coef: 해당 숫자에 더하는 수
      - numbers: coef의 숫자를 더할 수 있는 기존 숫자들의 집합
        (ex. -1을 더하기 위해서는 기존 숫자가 1이나 2여야 하므로 numbers[2]는 '12')
    """
    coef = [2, 1, -1, -2]
    numbers = ['0', '01', '12', '2']

    # 3진수에서 숫자 하나를 바꿔 만들 수 있는 수가 candidates에 있다면, 그 수를 리턴한다.
    for i in range(len(ternary) - 1, -1, -1):
        for j in range(4):
            if t_num + (coef[j] * 3 ** i) in candidates and ternary[T - 1 - i] in numbers[j]:
                return t_num + (coef[j] * 3 ** i)


T = int(input())

for tc in range(1, T + 1):
    binary = input()
    ternary = input()

    answer = get_answer(binary, ternary)
    print("#{} {}".format(tc, answer))
