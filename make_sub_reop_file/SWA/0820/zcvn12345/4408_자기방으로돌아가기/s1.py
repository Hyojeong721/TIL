import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cor = [0] * 200
    for i in range(N):
        start, end = map(int, input().split())
        if start <= end:
            for j in range((start-1)//2, (end-1)//2+1):
                cor[j] += 1
        else:
            for j in range((end-1)//2, (start-1)//2+1):
                cor[j] += 1
    print('#{0} {1}'.format(tc, max(cor)))