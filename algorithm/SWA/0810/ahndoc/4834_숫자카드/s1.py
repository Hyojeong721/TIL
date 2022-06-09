import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = int(input())
    count = [0] * 10

    for card in cards:
        count[int(card)] += 1

    max_card_count = count[0]
    max_card_number = 0
    for idx, val in enumerate(count):
        if val >= max_card_count:
            max_card_count = val
            max_card_number = idx

    print('#{} {} {}'.format(test_case, max_card_number, max_card_count))
