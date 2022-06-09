def itoa(nums):
    string = ''
    while nums // 10 >= 1:
        num = nums % 10
        nums = nums // 10
        string = chr(num+48) + string
    string = chr(nums+48) + string
    return string

print(itoa(125))