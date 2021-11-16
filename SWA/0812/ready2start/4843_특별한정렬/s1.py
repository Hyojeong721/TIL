import sys
sys.stdin = open("input.txt")


# 선택 정렬을 통해 요소가 N개인 배열 arr을 오름차순 정렬한다.
def selection_sort(arr, N):
    """선택 정렬을 통해 배열 arr을 오름차순 정렬한다.

    arr: 정렬하고자 하는 배열
    N: 배열의 길이
    min_idx: 매 정렬시 최소값의 인덱스
    """
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            # stable sort를 위해 <=가 아니라 <를 사용
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 배열 numbers를 오름차순 정렬한다.
    selection_sort(numbers, N)
    # new_arr: 특별한 정렬을 한 수들을 담은 배열
    new_arr = []

    for i in range(5):
        new_arr.append(numbers[N - i - 1])
        new_arr.append(numbers[i])

    print("#{} {}".format(tc, " ".join(str(x) for x in new_arr)))
