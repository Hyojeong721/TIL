import sys
sys.stdin = open('input.txt')

def partition(lst, l, r):
    comp = lst[l]
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= comp:
            i += 1
        while i <= j and lst[j] >= comp:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j

def quick_sort(lst, l=0, r=-10):
    if r == -10:
        r = len(lst) - 1
    if l < r:
        standard = partition(lst, l, r)
        quick_sort(lst, l, standard - 1)
        quick_sort(lst, standard + 1, r)



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input(). split()))
    quick_sort(lst)
    print('#{} {}'.format(tc, lst[N // 2]))
