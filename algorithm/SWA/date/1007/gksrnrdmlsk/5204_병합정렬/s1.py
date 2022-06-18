# 포기
import sys
sys.stdin = open('input.txt')

def merge(left, right):
    global big
    if left[-1] > right[-1]:
        big += 1
    n = 0
    cnt = 0
    left_length = len(left)
    right_length = len(right)
    lst = [0] * (len(left) + right_length)
    for i in range(left_length):
        if left[i] <= right[n]:
            lst[cnt] = left[i]
            cnt += 1
        else:
            while left[i] > right[n]:
                lst[cnt] = right[n]
                cnt += 1
                n += 1
                if n == right_length:
                    for j in range(i, left_length):
                        lst[cnt] = left[j]
                        cnt += 1
                    break
            if n == right_length:
                break

    if n != right_length:
        for i in range(n, right_length):
            lst[cnt] = right[i]
            cnt += 1
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
    print(merge_sort(lst))
    print(big)
