import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    num, N = input().split()
    num = list(map(int, ' '.join(num).split()))
    N = int(N)
    count = 0

    # while count < N:
    #     for i in range(N):
    #         max_idx = i
    #         if num[max_idx] == max(num):
    #             break
    #         for j in range(len(num)-1, i, -1):
    #             if num[j] > num[max_idx]:
    #                 max_idx = j
    #
    #         num[i], num[max_idx] = num[max_idx], num[i]
    #         count += 1

    print(num)
    print(count)



