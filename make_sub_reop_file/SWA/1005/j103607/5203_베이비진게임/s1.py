import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player1 = []
    player2 = []
    winner = 0
    for i in range(len(cards)):
        if i % 2 == 0:
            player1.append(cards[i])
            # triplet
            if player1.count(cards[i]) > 2:
                winner = 1
                break
            # run
            elif cards[i]+1 in player1 and cards[i]+2 in player1:
                winner = 1
                break
            elif cards[i]-1 in player1 and cards[i]+1 in player1:
                winner = 1
                break
            elif cards[i]-2 in player1 and cards[i]-1 in player1:
                winner = 1
                break

        else:
            player2.append(cards[i])
            # triplet
            if player2.count(cards[i]) > 2:
                winner = 2
                break
            # run
            elif cards[i] + 1 in player2 and cards[i] + 2 in player2:
                winner = 2
                break
            elif cards[i] - 1 in player2 and cards[i] + 1 in player2:
                winner = 2
                break
            elif cards[i] - 2 in player2 and cards[i] - 1 in player2:
                winner = 2
                break


    print('#{} {}'.format(tc, winner))