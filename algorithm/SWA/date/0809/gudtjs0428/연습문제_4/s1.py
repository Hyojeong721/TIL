nums = list(map(int, input()))

def if_babygin(nums):
    nums.sort()
    if nums[2] == nums[0] + 1:
        if nums[4] == nums[2] + 1:
            del nums[4]
            del nums[2]
            del nums[0]
    while nums and nums[0] == nums[1]:
        if nums[1] == nums[2]:
            for _ in range(3):
                del nums[0]
        break
    while nums and nums[1] == nums[0] + 1:
        if nums[2] == nums[1] + 1:
            for _ in range(3):
                del nums[0]
        break

    if nums:
        return 'no'
    return 'yes'

print(if_babygin(nums))