import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    cnt = 0
    for i in range(1, 1<<12):
        bitCnt = sum = 0
        for j in range(12):
            if i & (1<<j):
                sum += (j+1)
                bitCnt += 1
        if sum == K and bitCnt == N:
            cnt += 1

    print("#%d %d" % (tc, cnt))