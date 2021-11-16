import sys
sys.stdin = open(input.txt)

def winner_of_tournament(N, rcps):
    i = 1
    j = N
    js = []
    winners = []
    while (i + j) // 2 != 1:
        j = (i + j) // 2
        js.append(j)
    js.pop()

    #
    while js:
        if rcps[i-1] == rcps[i]:
            winners.append(i-1)
        elif rcps[i-1] == 1 and rcps[i] == 3:
            winners.append(i-1)
        elif rcps[i-1] < rcps[i]:
            winners.append(i)
        elif rcps[i-1] == 3 and rcps[i] == 1:
            winners.append(i)
        elif rcps[i-1] > rcps[i]:
            winners.append(i-1)
        js.pop()
        i += 2

    #
    while len(winners) != 1:
        for i in range(len(winners), 2):
            if rcps[winners[i]] == rcps[i+1]:
                winners.append(i)
            elif rcps[i] == 1 and rcps[i+1] == 3:
                winners.append(i)
            elif rcps[i] < rcps[i+1]:
                winners.append(i+1)
            elif rcps[i] == 3 and rcps[i+1] == 1:
                winners.append(i+1)
            elif rcps[i] > rcps[i+1]:
                winners.append(i)
            winners.pop()



    i = (1 + N) // 2 + 1
    j = N
    while (i + j) // 2 != 1:
        j = (i + j) // 2
        js.append(j)
    js.pop()
    while js:
        if rcps[i-1] == rcps[j-1]:
            winners.append(i-1)
        elif rcps[i-1] == 1 and rcps[j-1] == 3:
            winners.append(i-1)
        elif rcps[i-1] < rcps[j-1]:
            winners.append(j-1)
        elif rcps[i-1] == 3 and rcps[j-1] == 1:
            winners.append(j-1)
        elif rcps[i-1] > rcps[j-1]:
            winners.append(i-1)
        i += 2



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rcps = list(map(int, input().split()))
    print('#{} {}'.format(test_case, ))