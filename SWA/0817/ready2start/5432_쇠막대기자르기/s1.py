# 시간 초과 풀이

import sys
sys.stdin = open('input.txt')


def count_stick(brackets):
    """쇠막대기와 레이저의 배치를 나타내는 괄호 표현을 받아, 쇠막대기 조각의 개수를 구한다.

    조건 1: 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
    조건 2: 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
    조건 3: 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

    Args:
        brackets: 쇠막대기와 레이저의 배치를 나타내는 괄호 표현
            - '()': 레이저
            - '(': 쇠막대기의 시작
            - ')': 쇠막대기의 끝
    Returns:
        count: 쇠막대기 조각의 개수
    """
    # open_bracket_index: 닫히지 않은 여는 괄호들의 인덱스
    open_bracket_index = []
    count = 0

    # '()'를 '1'로 변환 ('1'의 위치: 레이저의 위치)
    sticks_and_razors = brackets.replace('()', '1')

    for idx, value in enumerate(sticks_and_razors):
        if value == '(':
            open_bracket_index.append(idx)
        elif value == ')':
            # start_idx: 현재 닫는 괄호와 매칭되는 여는 괄호의 인덱스
            start_idx = open_bracket_index.pop()
            # sub_count: 현재 탐색 중인 쇠막대기의 조각의 개수
            # 쇠막대기 조각의 개수 = 쇠막대기 인덱스 내의 '1'(레이저)의 개수 + 1
            sub_count = 1

            for i in range(start_idx + 1, idx):
                if sticks_and_razors[i] == '1':
                    sub_count += 1

            count += sub_count

    return count


T = int(input())

for tc in range(1, T + 1):
    # '()'를 '1'로 변환 ('1'의 위치: 레이저의 위치)
    brackets = input()

    stick_count = count_stick(brackets)
    print("#{} {}".format(tc, stick_count))
