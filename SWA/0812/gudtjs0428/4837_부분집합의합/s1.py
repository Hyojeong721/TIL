import sys
sys.stdin = open('input.txt')

def get_num_of_parts(N, K):
    nums = [i for i in range(1, 13)]
    parts = []
    part = []
    for i in range(1<<12):
        for j in range(12):
            if i & (1<<j):
                part.append(nums[j])
        parts.append(part)
        part =[]

    count = 0
    for part in parts:
        if len(part) == N and sum(part) == K:
            count += 1
    return count


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    print('#{} {}'.format(tc, get_num_of_parts(N, K)))