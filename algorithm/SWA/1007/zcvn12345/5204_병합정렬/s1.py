import sys
sys.stdin = open('input.txt')

T = int(input())

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = []
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            result.append(left.pop(0))
        elif right:
            result.append(right.pop(0))
    return result

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)



for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    r = merge_sort(nums)[N//2]
    print(f'#{tc} {cnt} {r}')
