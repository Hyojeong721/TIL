import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    existence = -1
    for i in range(1 << len(numbers)):
        sub_set = []
        for j in range(len(numbers)):
            if i & (1 << j):
                sub_set.append(numbers[j])
        if sum(sub_set) == 0:
            existence += 1

    if existence > 0:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')

