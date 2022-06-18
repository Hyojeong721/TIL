import sys
sys.stdin = open('input.txt')

def is_zero_subset(arr):
    cnt = 0
    for i in range(1 << 10):
        # 부분집합 1개 만들기 시작
        sub_sum = 0
        for j in range(10):
            if i & (1 << j):
                sub_sum += arr[j]
        # 완성된 부분집합 1개 원소들의 합이 0이면 1 반환
        # 원소가 하나도 없어서 합이 0인 경우 처리 위해 cnt 셈
        if sub_sum == 0:
            cnt += 1
            if cnt == 2:
                return 1

    # 합이 0인 부분집합 없이 끝나면 0 반환
    return 0

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    result = is_zero_subset(arr)
    print('#{0} {1}'.format(tc, result))