import sys
sys.stdin = open("input.txt")


def get_winner(cards, start, end):
    """
    인원수와 카드 목록을 인자로 받아, 토너먼트 카드게임의 승자를 찾는다.
      - 카드 숫자는 각각 1이 가위, 2가 바위, 3이 보를 나타낸다.
      - 같은 카드인 경우 번호가 작은 쪽이 이긴다.

    Args:
        cards: 각 학생이 가진 카드의 번호
        start: 첫번째 학생의 번호
        end: 마지막 학생의 번호
    Returns:
        최종 승자의 번호
    """
    # base case: 참가자 수가 1명인 경우
    if start == end:
        return start

    mid = (start + end) // 2
    # left: 반으로 잘랐을 때 왼쪽 부분의 승자 번호
    left = get_winner(cards, start, mid)
    # right: 반으로 잘랐을 때 오른쪽 부분의 승자 번호
    right = get_winner(cards, mid + 1, end)

    # 오른쪽 참가자가 이긴 경우 => 오른쪽 참가자를 리턴한다.
    if (cards[left], cards[right]) in ((1, 2), (2, 3), (3, 1)):
        return right
    # 왼쪽 참가자가 이기거나 비긴 경우 => 왼쪽 참가자를 리턴한다.
    return left


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 1번 인덱스부터 시작하기 위해 0번째 인덱스에 -1을 지정한다.
    cards = [-1] + [int(x) for x in input().split()]

    winner_number = get_winner(cards, 1, N)
    print("#{} {}".format(tc, winner_number))
