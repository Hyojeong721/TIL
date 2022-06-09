import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    t = input()
    nums = list(map(int, input().split()))
    while nums[-1] > 0:
        for i in range(1, 6):
            if nums[-1] > 0:
                a = nums.pop(0) - i
                nums.append(a)
            else:
                break
    nums[-1] = 0
    print(f'#{tc}', end=' ')
    for i in nums:
        print(i, end=' ')
    print()


