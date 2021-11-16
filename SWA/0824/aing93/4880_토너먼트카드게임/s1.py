import sys
sys.stdin = open('input.txt')

def whowins(num1, num2):
    if cards[num1] == cards[num2]:
        return [min(num1, num2)]
    elif abs(cards[num1]-cards[num2]) == 1:
        if cards[num1] > cards[num2]:
            return [num1]
        else:
            return [num2]
    elif abs(cards[num1]-cards[num2]) == 2:
        if cards[num1] < cards[num2]:
            return [num1]
        else:
            return [num2]

def divide(nums):
    if len(nums) == 1:
        return nums

    middle = (len(nums)-1)//2+1
    front = nums[:middle]
    rear = nums[middle:]

    front = divide(front)
    rear = divide(rear)

    return whowins(front[0], rear[0])

T = int(input())
for test_case in range(1, T + 1):
    numcard = int(input())
    cards = list(map(int,(input().split())))
    nums = list(range(numcard))
    print(nums)
    ans = divide(nums)[0] + 1
    print(ans)
    print('#{} {}'.format(test_case, divide(nums)[0]+1))

