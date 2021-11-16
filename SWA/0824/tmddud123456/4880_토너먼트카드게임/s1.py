import sys
sys.stdin = open('input.txt')

def half(people):
    if len(people) == 1:
        return people[0]
    elif len(people) == 2:
        return rsp(people[0], people[1])
    else:
        n = len(people)

        a = half(people[0:(n//2)])
        b = half(people[(n//2):n])
        return rsp(a, b)

def rsp(a, b):      # rock, sissors, paper 가위바위보
    card1 = cards[a-1]
    card2 = cards[b-1]

    if card1 >= card2:
        if card1 - card2 == 2:
            return b
        else:
            return a
    if card1 < card2:
        if card2 - card1 == 2:
            return a
        else:
            return b


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    people = [0]*N
    for i in range(N):
        people[i] = i+1
    print('#{} {}'.format(tc, half(people)))
