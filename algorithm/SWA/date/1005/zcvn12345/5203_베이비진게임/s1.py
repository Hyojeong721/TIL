import sys
sys.stdin = open('input.txt')

T = int(input())

def BabyJin(player):
    for j in range(10):
        if player[j]:
            if player[j] >= 3:
                return True
            elif j <= 7 and player[j] and player[j+1] and player[j+2]:
                return True
    return False

def Game(cards):
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(12):
        if i % 2 == 0:
            player1[cards[i]] += 1
            if BabyJin(player1):
                return 1
        else:
            player2[cards[i]] += 1
            if BabyJin(player2):
                return 2
    return 0

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    print(f'#{tc} {Game(cards)}')