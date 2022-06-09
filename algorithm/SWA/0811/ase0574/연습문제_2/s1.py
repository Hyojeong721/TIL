import sys
sys.stdin = open('input.txt')

#부분집합의 합이 0이 되는 것이 존재하는지 출력하는 코드 작성

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr) #원소의 개수 : n

    # 공집합 제외하려고 시작점 1로 설정/(1~부분집합개수)
    for i in range(1, 1<<n):
        total = 0
        for j in range(n):

            #부분집합 원소들의 합을 total에 저장
            if i & (1<<j):
                total += arr[j]

        #합이 0인 경우 반복문 정지!
        if total == 0:
            result = 1
            break

        else:
            result = 0

    print('#{} {}'.format(tc, result))


