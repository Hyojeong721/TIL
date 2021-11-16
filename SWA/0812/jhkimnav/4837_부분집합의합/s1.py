import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    answer = 0
    # N : 부분집합 원소의 수, K :부분 집합의 합
    N, K = list(map(int, input().split()))
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    for i in range(1 << len(arr)):
        sum = 0
        for j in range(N+1):
            if i & (1 << j):
                # print(arr[j], end=", ")
                sum += arr[j]
                if sum == K:
                    answer += 1
                    break
    #     print()
    # print()
                # sum += arr[j]
                # if sum == 0:
                #     answer = 1
                #     break

    print('#{} {}'.format(test_case, answer))
