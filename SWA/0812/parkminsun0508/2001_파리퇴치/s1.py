# 2001 파리퇴치
# 죽은 파리의 개수 구하기

import sys
sys.stdin = open("input.txt")

# 테스트 케이스 개수를 받아온다.
T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    result = 0
    for n in range(N):
        numbers = list(map(int, input().split()))
        arr.append(numbers)

    sum_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for r in range(i, i+M):
                for l in range(j, j+M):
                    sum += arr[r][l]
            sum_list.append(sum)
    for i in range(len(sum_list)):
        if sum_list[i] > result:
            result = sum_list[i]
    print("#{} {}".format(tc, result))