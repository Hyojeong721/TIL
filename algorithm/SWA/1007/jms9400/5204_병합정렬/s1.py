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
    result = []

    if lst1[-1] > lst2[-1]:
        cnt += 1

    i, j = 0, 0

    while len(lst1) > i and len(lst2) > j:
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    if len(lst1) > i:
        result += lst1[i:]
    if len(lst2) > j:
        result += lst2[j:]

    return result


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우

    arr = mergesort(arr)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))