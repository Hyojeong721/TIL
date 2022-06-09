import sys
sys.stdin = open('input.txt')

# 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 = cnt
def merge_sort(arr):
    global cnt

    # 원소 한개인 경우
    if len(arr) == 1:
        return arr

    # 여러개 들어있는 경우
    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merge_list = []
    l = h = 0
    while len(left) > l and len(right) > h:
        # 왼쪽이 더 큰 경우
        if left[l] <= right[h]:
            merge_list.append(left[l])
            l += 1
        # 오른 쪽이 더 큰 경우
        else:
            merge_list.append(right[h])
            h += 1

    # 비교할 대상없이 남은거 다 집어넣기
    if len(left) > l:
        merge_list.extend(left[l:])
        cnt += 1
    else:
        merge_list.extend(right[h:])

    return merge_list


T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))

    ans = merge_sort(arr)

    #  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력
    print('#{} {} {}'.format(tc, ans[N//2], cnt))



add = [1, 2]
item = [9, 8, 7, 6]
add.append(item[:2])
print(add)
add.extend(add[1])
print(add)
