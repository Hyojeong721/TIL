import sys
sys.stdin = open(input.txt)

def winner_of_tournament(N, rcps):
    i = 1
    j = N
    # int(루트2) - 1 만큼 반갈 행위를 해서 첫 대진표 완성
    winners = get_winners(i, j, rcps)
    if len(winners) == 1:
        return winners[0]
    else:
        get_winners(i, j, rcps)

def get_winners(i, j, rcps):
    half = (i + j) // 2






T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rcps = list(map(int, input().split()))
    print('#{} {}'.format(test_case, ))