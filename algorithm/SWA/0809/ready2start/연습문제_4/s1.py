import sys
sys.stdin = open('input.txt')

"""
[run보다 triplet을 먼저 처리하는 이유]

ex) 5 5 5 6 7 8

위 경우는 baby-gin이지만, run을 먼저 처리할 경우 5 6 7을 먼저 처리하고,
남은 5 5 8은 run이나 triplet이 아니므로 baby-gin이 아니라고 판단할 위험이 있다.
"""


def check_baby_gin(cards):
    """
    주어진 6장의 카드가 baby-gin인지 확인한다.
        - baby-gin: 6장의 카드가 run과 triplet으로만 구성된 경우
        - run: 3장의 카드가 연속적인 번호를 갖는 경우
        - triplet: 3장의 카드가 동일한 번호를 갖는 경우

    cards: 6장의 카드 번호 (배열)
    counts: 0~9의 숫자당 카드의 개수
    """
    counts = [0] * 10

    for i in range(6):
        temp = int(numbers[i])
        counts[temp] += 1

    # 1. triplet 처리
    for i in range(10):
        counts[i] %= 3

    # 2. run 처리
    for i in range(8):
        while counts[i] and counts[i + 1] and counts[i + 2]:
            counts[i] -= 1
            counts[i + 1] -= 1
            counts[i + 2] -= 1

    # 3. baby-gin 여부 판단
    # counts 배열의 값이 모두 0이면 True, 아니면 False
    for i in range(10):
        if counts[i]:
            return False
    return True


N = int(input())

for _ in range(N):
    numbers = input()
    print(check_baby_gin(numbers))
