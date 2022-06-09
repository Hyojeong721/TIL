import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 신청서 개수
    applications = [list(map(int, input().split())) for _ in range(N)]
    accepted = []
    accepted2 = []

    i = 24
    while i > 0:
        tmp = []
        for application in applications:
            if application[1] == i:
                tmp.append(application)
        if tmp:
            long = 0
            for application in tmp:
                if application[0] > long:
                    long = application[0]
            accepted.append([long, i])
            i = long
        else:
            i -= 1

    j = 0
    while j < 24:
        tmp = []
        for application in applications:
            if application[0] == j:
                tmp.append(application)
        if tmp:
            short = 24
            for application in tmp:
                if application[1] < short:
                    short = application[1]
            accepted2.append([j, short])
            j = short
        else:
            j += 1

    result = max(len(accepted), len(accepted2))
    print(accepted)
    print(accepted2)
    print(f'#{tc} {result}')


