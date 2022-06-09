def is_run_triplet(nums):
    tri = 1
    run1 = 0
    run2 = 0
    for i in range(1, 3):
        if nums[i] == nums[0]:
            tri += 1
        if int(nums[i]) == int(nums[i-1]) - 1:
            run1 += 1
        elif int(nums[i]) == int(nums[i - 1]) + 1:
            run2 += 1
    if tri == 3 or run1 == 2 or run2 == 2:
        return True
    else:
        return False


def perm(n, k):
    global is_babygin
    if k == n:
        nums = ''.join(p)
        ans = is_run_triplet(nums[:3]) * is_run_triplet(nums[3:])
        if ans:
            is_babygin = True
        return
    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(n, k + 1)
            p[k], p[i] = p[i], p[k]


lst = ['124783', '667767', '054060', '101123']
for nums in lst:
    p = list(nums)
    is_babygin = False
    perm(6, 0)
    print('{}이 babygin: {}'.format(p, is_babygin))