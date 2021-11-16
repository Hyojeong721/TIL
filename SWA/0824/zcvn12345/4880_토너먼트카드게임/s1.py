import sys
sys.stdin = open('input.txt')


def rcp(cards, player1, player2):
    if cards[player1] == 1 and cards[player2] == 2:
        return player2
    elif cards[player1] == 2 and cards[player2] == 3:
        return player2
    elif cards[player1] == 3 and cards[player2] == 1:
        return player2
    else:
        if player1 < player2:
            return player1
        else:
            player2


def tournament(cards, students):
    winner = []
    if len(students) == 1:
        print(students[0]+1)
    else:
        if len(students) % 2:
            for i in range(0, len(students)-1, 2):
                winner.append(rcp(cards, students[i], students[i+1]))
            winner.append(students[-1])
            tournament(cards, winner)
        else:
            for i in range(0, len(students), 2):
                winner.append(rcp(cards, students[i], students[i+1]))
            tournament(cards, winner)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    S = [i for i in range(N)]
    C = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    tournament(C, S)







