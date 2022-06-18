import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, nums = input().split()
    ans = ''
    for num in nums:
        bi = format(int(num, 16), 'b')
        ans += '0' * (4 - len(bi)) + bi
        # ans += bi.zfill(4)

    print('#{} {}'.format(tc, ans))