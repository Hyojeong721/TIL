import sys
sys.stdin = open('input.txt')
# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

T = int(input())

for tc in range(1,T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int,input().split()))

    temp = []
    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += arr[i+j]
        temp.append(total)

    max_total = temp[0]
    min_total = temp[0]
    for i in range(len(temp)):
        if max_total < temp[i]:
            max_total = temp[i]
        if min_total > temp [i]:
            min_total = temp[i]

    result = max_total - min_total
    print("#{} {}".format(tc,result))
