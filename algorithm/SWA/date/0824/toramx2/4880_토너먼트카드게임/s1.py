import sys
sys.stdin = open('input.txt')

def grouping(start, end):
    # 그룹에 1명이 있을 때
    if start == end:
        return start
    # 그룹에 이웃한사람 2명이 있을 때
    elif start == end - 1:
        return rsp(start, end)
    # 그룹에 3명 이상일 때
    else:
        group1 = grouping(start, (start+end)//2)
        group2 = grouping((start+end)//2 + 1, end)
        return rsp(group1, group2)

def rsp(player1, player2):
    # player2 가 이기는 경우
    if (card[player1] == 1 and card[player2] == 2 or
        card[player1] == 2 and card[player2] == 3 or
        card[player1] == 3 and card[player2] == 1):
        return player2
    # player1가 이기는 경우, 비기는 경우
    else:
        return player1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    card.insert(0, 0)

    print('#{} {}'.format(test_case, grouping(1, N)))
