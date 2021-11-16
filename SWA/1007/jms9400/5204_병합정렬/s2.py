import sys
sys.stdin = open('input.txt')

T = int(input())

def mergesort(lst):

    n = len(lst)
    if n == 1:
        return lst

    lst1 = mergesort(lst[:n//2])
    lst2 = mergesort(lst[n//2:])

    return merge(lst1, lst2)

def merge(lst1, lst2):
    global cnt

    if lst1[-1] > lst2[-1]:
        cnt += 1

    result = lst1+lst2
    result.sort()
    return result


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우

    arr = mergesort(arr)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))