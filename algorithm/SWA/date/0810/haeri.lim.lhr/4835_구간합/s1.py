import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):

    N, M = list(map(int,input().split()))
    temp = list(map(int,input().split()))

    max_sum, min_sum = 0, 0

    for j in range(M):
        min_sum += temp[j]

    for i in range(N-M+1):
        M_sum = 0
        for j in range(M):
            M_sum += temp[i+j]

        if M_sum >= max_sum:
            max_sum = M_sum
        elif M_sum <= min_sum:
            min_sum = M_sum

    print('#%d %d' % (test_case, max_sum - min_sum))