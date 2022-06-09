# deque 으로 하는 법
import sys
sys.stdin = open('input.txt')
from collections import deque


# 두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
def merge(left, right):
    result = []
    left = deque(left)
    right = deque(right)
    # 각각의 최소값들(가장 왼쪽 값)을 비교해서 더 작은 요소를 result에 추가

    # 두 부분집합에 원소가 없어질 때까지 반복
        # 두 부분집합이 모두 남아 있으면

    while left and right:
        # 왼쪽이 작을 때
        if left[0] <= right[0]:
            result.append(left.popleft())
        # 오른쪽이 작을 때
        else:
            result.append(right.popleft())
    # 왼쪽만 남아 있으면
    if left:
        result.extend(left)
    # 오른쪽만 남아 있으면
    if right:
        result.extend(right)

    return result

def merge_sort(arr):
    global cnt
    # arr를 반씩 나누어서 하나 남을때 까지 나누기
    if len(arr) == 1: # 하나 남을때
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        if left[-1] > right[-1]:
            cnt += 1
    # 합치기
    return merge(left, right)

# arr1 = [69, 10, 30, 2, 16, 8, 31, 22]
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))
    arr = merge_sort(arr)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))

