import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    card_list = [0] * 10

    cards = input()
    for card in cards:
        card_list[int(card)] += 1

    tmp_cnt = card_list[0]
    tmp_idx = 0
    for idx, cnt in enumerate(card_list[1:], start=1):
        if tmp_cnt <= cnt:
            tmp_cnt = cnt
            tmp_idx = idx

    print('#{} {} {}'.format(t, tmp_idx, tmp_cnt))