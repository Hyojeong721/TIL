import sys
sys.stdin = open('input.txt')


def is_run_triplet(lst):
    """
    현재 리스트에 run 또는 triplet이 있는지 검사

    """
    if 3 in lst:
        return True
    for i in range(8):
        if lst[i] and lst[i+1] and lst[i+2]:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    for idx, card in enumerate(cards):
        if not idx % 2:
            p1[card] += 1
        else:
            p2[card] += 1

        if idx >= 4 and is_run_triplet(p1):
            winner = 1
            break
        if idx >= 5 and is_run_triplet(p2):
            winner = 2
            break

    print('#{} {}'.format(tc, winner))