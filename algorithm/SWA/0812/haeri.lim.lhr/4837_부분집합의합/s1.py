import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):

    N, K = list(map(int, input().split()))
    # 1~12 까지 배열 생성
    arr = list(range(1, 13))

    # 개수 저장하는 count 변수 선언
    count = 0

    #모든 부분집합을 생성
    for i in range(1<<len(arr)):

        # 부분 집합을 저장하는 배열 temp선언
        temp = []

        # 부분집합의 합을 저장하는 total 변수 선언
        total = 0
        for j in range(len(arr)):
            if i & (1 << j):
                temp.append(arr[j])
        # 부분집합의 합
        for k in temp:
            total += k
        # 조건에 맞는 부분집합의 개수
        if total == K and len(temp) == N:
            count += 1

    print('#%d %d' %(test_case, count))