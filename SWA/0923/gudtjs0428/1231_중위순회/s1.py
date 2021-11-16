import sys
sys.stdin = open('input.txt')

# 왼쪽 밑부터 시작하려다.... 너무 안되네

def to_string(N, n, info):
    global string
    string += info[n][1]
    tmp = n + 1
    n //= 2
    if len(info[n]) == 4 and len(info[tmp]) > 2:
        while tmp < N and len(info[tmp]) > 2:
            tmp = tmp * 2
        n = tmp
        to_string(N, n, info)
    else:
        if info[n]:
            to_string(N, n, info)
        else:
            string += info[n][1]
            info[n] = 0
            string += info[tmp][1]
            info[tmp] = 0



T = 10
for test_case in range(1, T + 1):
    N = to_cal_multip = int(input())
    info = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        info[i] = input().split()
    multipli = 0
    while to_cal_multip > 1:
        to_cal_multip //= 2
        multipli += 1
    start = 2 ** multipli
    string = ''
    to_string(N, start, info)
    print('#{} {}'.format(test_case, string))