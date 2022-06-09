import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    W = sorted(list(map(int, input().split())), reverse=True)
    T = sorted(list(map(int, input().split())), reverse=True)

    idx = 0
    for i in range(N):
        if W[i] > T[0]:
            idx = i+1
    W = W[idx:N]
    N = len(W)

    result = 0
    for i in range(min(N, M)):
        if W[i] <= T[i]:
            result += W[i]
        else:
            pass
    print('#{} {}'.format(test_case, result))