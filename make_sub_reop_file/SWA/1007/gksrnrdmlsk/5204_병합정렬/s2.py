import sys
sys.stdin = open('input.txt')

def merge(left, right):
    global big
    if left[-1] > right[-1]:
        big += 1
    lst = []
    left_length = len(left)
    right_length = len(right)
    n = 0
    for i in range(left_length):
        if left[i] <= right[n]:
            lst.append(left[i])
        else:
            while n < right_length and left[i] > right[n]:
                lst.append(right[n])
                n += 1
            if n == right_length:
                return lst + left[i:]
            lst.append(left[i])

    if n < right_length:
        return lst + right[n:]

    return lst


def merge_sort(lst):
    length = len(lst)
    if length == 1:
        return lst
    else:
        left = lst[:length//2]
        right = lst[length//2:]
        return merge(merge_sort(left), merge_sort(right))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    big = 0
    print('#{} {} {}'.format(tc, merge_sort(lst)[N//2], big))
