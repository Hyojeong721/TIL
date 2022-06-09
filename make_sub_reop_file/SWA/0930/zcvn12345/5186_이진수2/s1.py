import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    cnt = 0
    result = ''
    while N != 0.0:
        N = N * 2
        if N >= 1:
            N -= 1
            result += '1'
        else:
            result += '0'
        cnt += 1
    if cnt > 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')