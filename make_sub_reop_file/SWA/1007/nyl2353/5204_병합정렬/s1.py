import sys
sys.stdin = open('input.txt')


def merge_sort(lst):
    global left_bigger

    if len(lst) <= 1:
        return lst

    left = merge_sort(lst[:len(lst)//2])
    right = merge_sort(lst[len(lst)//2:])
    if left[-1] > right[-1]:
        left_bigger += 1

    return merge(left, right)

def merge(left, right):
    sorted_lst = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_lst.append(right[j])
            j += 1
        else:
            sorted_lst.append(left[i])
            i += 1

    while i < len(left):
        sorted_lst.append(left[i])
        i += 1

    while j < len(right):
        sorted_lst.append(right[j])
        j += 1

    return sorted_lst


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    left_bigger = 0
    sorted_lst = merge_sort(lst)

    print('#{} {} {}'.format(tc, sorted_lst[N//2], left_bigger))