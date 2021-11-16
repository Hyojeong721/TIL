import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    set_info = list(map(int, input().split()))
    original_set = list(range(1, 13))
    result = 0

    for i in range(1 << 12):
        sub_sets = []
        for j in range(12):
            if i & (1 << j):
                sub_sets.append(original_set[j])

        if len(sub_sets) == set_info[0] and sum(sub_sets) == set_info[1]:
            result += 1

    print(f'#{tc} {result}')





