import sys
sys.stdin = open('input.txt')

def get_change_to_most(nums, times):
    num_list = [int(n) for n in nums]
    times = int(times)
    length = len(nums)
    cnt = 0
    i = 0
    while cnt < times and i < length:
        max_i = i
        for j in range(i+1, length):
            if num_list[j] >= num_list[max_i]:
                max_i = j
        if max_i != i:
            cnt += 1
        num_list[i], num_list[max_i] = num_list[max_i], num_list[i]
        i += 1
    if length % 2 and cnt == length // 2:
        return num_list[:length//2+1] + sorted(num_list[length//2+1:],reverse=True)
    resi_cnt = times - cnt
    if resi_cnt and resi_cnt % 2:
        for i in range(10):
            if num_list.count(i) > 1:
                return num_list
        else:
            num_list[-2], num_list[-1] = num_list[-1], num_list[-2]
    return num_list


T = int(input())
for test_case in range(1, T + 1):
    nums, times = input().split()
    changed_num = get_change_to_most(nums, times)
    print('#{}'.format(test_case), end=' ')
    for n in changed_num:
        print(n,end='')
    print()