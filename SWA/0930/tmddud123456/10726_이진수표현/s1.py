import sys
sys.stdin = open('input.txt')

def checkOnOff():
    global N, temp
    if len(temp) < N:
        return 'OFF'
    for i in range(len(temp)-1, len(temp)-1-N, -1):
        if temp[i] != '1':
            return 'OFF'
    return 'ON'


TC = int(input())

for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))
    temp = str(format(int(M), 'b'))

    print(f'#{tc} {checkOnOff()}')