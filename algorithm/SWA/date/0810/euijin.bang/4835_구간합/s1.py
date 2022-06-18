import sys
sys.stdin = open('input.txt')

T = int(input())

# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력

# N : N개의 정수가 들어있는 베열
# M : 이웃한 M개의 합
# 합이 가장 큰 경우와 가장 작은 경우의 차이

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sumList = []

    for i in range(0, N - M + 1):
        sumList.append(sum(arr[i:i + M]))

    ans = max(sumList) - min(sumList)

    print("#{} {}".format(tc, ans))
