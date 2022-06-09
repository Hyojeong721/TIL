import sys
sys.stdin = open('input.txt')

T = int(input())

def max_card(cards):
    count_cards = [0] * 10
    for card in cards:
        count_cards[card] += 1

    count_num = 0
    most_num = 0
    for idx, count in enumerate(count_cards):
        if count >= count_num:
            count_num = count
            most_num = idx
    return most_num, count_num


for tc in range(1, T + 1):
    N = input()
    cards = []
    for num in input():
        cards.append(int(num))
    # most.append(map(lambda x:int(x), input()))
    print('#{0} {1} {2}'.format(tc, max_card(cards)[0], max_card(cards)[1]))