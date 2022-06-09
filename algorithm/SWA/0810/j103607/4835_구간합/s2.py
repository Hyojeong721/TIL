import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))


    # 구간합 리스트 만들기
    sum_list = []
    for i in range(N-M+1):
        sumV = 0
        for j in range(M):
            sumV += num_list[i+j]
        sum_list.append(sumV)

    # 구간합 중에서 최대값/최소값 구하기
    maxV = sum_list[0]
    minV = sum_list[0]
    for i in sum_list:
        if maxV <= i:
            maxV = i
        elif minV > i:
            minV = i

    # 최대값-최소값 출력
    print('#{} {}'.format(tc, maxV-minV))