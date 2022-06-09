import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    num = int(input())
    print(num)

    cnt = [0] * 10
    for i in range(6):
        tmp = num % 10
        cnt[tmp] += 1
        num //= 10

    j = 0
    triplet = run = 0
    while j < 10:
        if cnt[j] >= 3:
            cnt[j] -= 3
            triplet += 1
            continue
        if cnt[j-2] >= 1 and cnt[j-1] >= 1 and cnt[j] >= 1:
            cnt[j-2] -= 1
            cnt[j-1] -= 1
            cnt[j] -= 1
            run += 1
            continue
        j += 1

    result = '0'
    if run+triplet == 2:
        result = 'babygin'
    print('#{} {}'.format(t, result))