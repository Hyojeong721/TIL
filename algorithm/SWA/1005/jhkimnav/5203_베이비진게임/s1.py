import itertools
import sys
sys.stdin = open('input.txt')


def is_run_or_triplet(card_list):
    cnt = 0
    for card in card_list:
        # Check RUN
        if card[0] + 1 == card[1] and card[1] + 1 == card[2]:
            cnt += 1
            break

        # Check Triplet
        if card[0] == card[1] and card[1] == card[2]:
            cnt += 1
            break

    return cnt


T = int(input())

for tc in range(1, T+1):
    card_list = list(map(int, input().split()))

    player1 = []
    player2 = []
    win_player = 0

    for i in range(len(card_list) // 2):
        player1.append(card_list[i*2])
        player2.append(card_list[(i*2) + 1])
        if i >= 2:
            nPr1 = list(itertools.permutations(player1, 3))
            nPr2 = list(itertools.permutations(player2, 3))
            print(nPr2)

            if is_run_or_triplet(nPr1):
                win_player = 1
                break

            elif is_run_or_triplet(nPr2):
                win_player = 2
                break

    print('#{} {}'.format(tc, win_player))