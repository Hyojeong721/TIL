import sys
sys.stdin = open('input.txt')

def winner_of_tournament(N, rcps):
    # int(루트2) - 1 만큼 반갈 행위를 해서 첫 대진표 완성
    # 재귀 도저히 모르겠다
    js = [N]
    get_js(1, N, N, js)
    js.sort()

    winners = [i for i in range(1, N, 2)]
    while js:
        if rcps[winners[0]] == rcps[js[0]]:
            winners.append(winners[0])
        elif rcps[winners[0]] == 1 and rcps[js[0]] == 3:
            winners.append(winners[0])
        elif rcps[winners[0]] < rcps[js[0]]:
            winners.append(js[0])
        elif rcps[winners[0]] == 3 and rcps[js[0]] == 1:
            winners.append(js[0])
        elif rcps[winners[0]] > rcps[js[0]]:
            winners.append(winners[0])
        del winners[0]
        del js[0]

    while len(winners) != 1:
        if len(winners) % 2:
            for i in range(0, len(winners) - 1, 2):
                if rcps[winners[i]] == rcps[winners[i+1]]:
                    winners.append(winners[i])
                elif rcps[winners[i]] == 1 and rcps[winners[i+1]] == 3:
                    winners.append(winners[i])
                elif rcps[winners[i]] < rcps[winners[i+1]]:
                    winners.append(winners[i+1])
                elif rcps[winners[i]] == 3 and rcps[winners[i+1]] == 1:
                    winners.append(winners[i+1])
                elif rcps[winners[i]] > rcps[winners[i+1]]:
                    winners.append(winners[i])
                del winners[0], winners[0]
        else:
            for i in range(0, len(winners), 2):
                if rcps[winners[i]] == rcps[winners[i+1]]:
                    winners.append(winners[i])
                elif rcps[winners[i]] == 1 and rcps[winners[i+1]] == 3:
                    winners.append(winners[i])
                elif rcps[winners[i]] < rcps[winners[i+1]]:
                    winners.append(winners[i+1])
                elif rcps[winners[i]] == 3 and rcps[winners[i+1]] == 1:
                    winners.append(winners[i+1])
                elif rcps[winners[i]] > rcps[winners[i+1]]:
                    winners.append(winners[i])
                del winners[0], winners[0]
    return winners[0]


def get_js(i, j, N, js):
    half = (i + j) // 2
    if half != 1:
        js.append(half)
        get_js(i, half, N, js)
    if half + 1 != N:
        js.append(half)
        get_js(i, half, N, js)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rcps = [0]
    rcps.extend(map(int, input().split()))
    print('#{} {}'.format(test_case, winner_of_tournament(N, rcps)))