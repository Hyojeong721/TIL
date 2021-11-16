import sys
sys.stdin = open('input.txt')


def card_game(cards, start, end):
    """
    카드의 start ~ end 인덱스 중 승자를 겨루는 게임

    :param cards: 전체 카드
    :param start: 시작 인덱스
    :param end: 종료 인덱스
    :return: 승자의 인덱스

    """
    win_case = {1: 3, 2: 1, 3: 2}

    # 1명 => 해당 인덱스 반환
    if end == start:
        return start

    # 2명 => 비교 후, 승자의 인덱스 반환
    elif end - start == 1:
        if cards[start] == cards[end]:
            return start
        elif win_case[cards[start]] == cards[end]:
            return start
        else:
            return end

    # 3명 이상이면 그룹 쪼갬
    else:
        win1 = card_game(cards, start, (start + end)//2)
        win2 = card_game(cards, (start + end)//2 + 1, end)
        if cards[win1] == cards[win2]:
            return win1
        elif win_case[cards[win1]] == cards[win2]:
            return win1
        else:
            return win2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    # 사람은 1번부터 시작
    result = card_game(cards, 0, N - 1) + 1
    print('#{} {}'.format(tc, result))