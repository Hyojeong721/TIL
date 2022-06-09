import sys
sys.stdin = open('input.txt')


def duel(left, right):
    """
    :param left: 왼쪽 학생의 idx 번호
    :param right: 오른쪽 학생의 idx 번호
    :return win: 이긴 학생의 idx 번호

    가위바위보의 승자를 판단
    """
    player1 = cards[left - 1]   # 왼쪽 학생의 카드
    player2 = cards[right - 1]   # 오른쪽 학생의 카드
    print(player1, player2)

    # 1: 가위, 2: 바위, 3: 보
    ## 기본적으로 숫자가 크면 이김 ( 1(가위)과 3(보) 제외 )
    if player1 > player2:
        win = left
        if player1 == 3 and player2 == 1:
            win = right

    elif player1 < player2:
        win = right
        if player1 == 1 and player2 == 3:
            win = left

    elif player1 == player2:
        win = left

    return win


def half(left, right):
    """
    :param left: 왼쪽 학생의 idx 번호
    :param right: 오른쪽 학생의 idx 번호
    :return left: 최소단위까지 쪼개진 경우 이를 반환, 다음 함수 계산에 사용
    :return duel(): 함수 계산 후 win(이긴 학생의 idx번호) 반환

    학생 리스트를 분할 후, 카드 비교에서 이긴 학생의 idx 반환
    이긴 학생의 idx가 저장된 win 변수를 반복 갱신
    최소단위의 경우 최소단위 학생 idx 반환
    """
    mid = (left + right) // 2

    # 최소단위
    if left == right:
        return left

    # 왼쪽과 오른쪽으로 학생 나눈 후, 각각 분할 반복
    left_half = half(left, mid)
    right_half = half(mid + 1, right)

    return duel(left_half, right_half)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards =list(map(int, input().split()))
    print(cards)
    print('#{} {}'.format(t, half(1, N)))