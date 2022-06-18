import sys
sys.stdin = open('input.txt')

T = int(input())

def district_dif(N, M, nums):
    totals = []
    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += nums[i+j]
        totals.append(total)

    max_total = min_total = totals[0]
    for total in totals:
        if total > max_total:
            max_total = total
        elif total < min_total:
            min_total = total
    return max_total - min_total

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    print('#{0} {1}'.format(tc, district_dif(N, M, nums)))