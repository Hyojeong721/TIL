import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for i in range(M):
        a = data.pop(0)
        data.append(a)

    print('#{} {}'.format(tc, data[0]))
