import sys
sys.stdin = open('input.txt')
triples = [(i, (i + 1) % 10, (i + 2) % 10) for i in range(10)]

def is_bg(cards):
    lst = [0] * 10
    for i in cards:
        lst[i] += 1
        if lst[i] >= 3:
            return True
    for j in triples:
        if lst[j[0]] >= 1 and lst[j[1]] >= 1 and lst[j[2]] >= 1:
            return True
    return False

T = int(input())
for tc in range(1, T + 1):
    whole_cards = list(map(int, input().split()))[:]
    cards_1 = [whole_cards[2 * i] for i in range(6)]
    cards_2 = [whole_cards[2 * i + 1] for i in range(6)]
    answer = 0
    for step in range(3, 7):
        if is_bg(cards_1[:step]):
            answer = 1
            break
        if is_bg(cards_2[:step]):
            answer = 2
            break

    print('#{} {}'.format(tc, answer))