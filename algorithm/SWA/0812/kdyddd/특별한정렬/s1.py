import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    num = int(input())
    nums = list(map(int, input().split()))

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


    answer = ''
    num_length = len(nums) // 2

    cnt = 0
    for i in range(num_length):
        answer += str(nums[num_length * 2 - 1 - i]) + ' ' + str(nums[i]) + ' '
        cnt += 2
        if cnt == 10:
            break

    if cnt != 10 and len(nums) % 2 != 0:
        answer += str(nums[len(nums)])
    else:
        answer = answer[:-1]

    print(f'#{test_case} {answer}')





