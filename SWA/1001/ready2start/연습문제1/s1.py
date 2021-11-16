
def selection_sort(arr, start):
    """
    선택 정렬 알고리즘을 통해, 주어진 배열을 오름차순 정렬한다.
    Args:
        arr: 정렬할 배열
        start: 정렬이 완료되지 않은 첫번째 인덱스
    """
    # basis part: 정렬이 완료되지 않은 원소가 1개 이하인 경우
    if start >= len(arr) - 1:
        return

    # min_idx: 최소값이 저장된 인덱스
    min_idx = start

    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    # 배열의 최소값을 맨 앞 요소와 바꾸어준다.
    arr[start], arr[min_idx] = arr[min_idx], arr[start]

    # 정렬된 0번 인덱스를 제외한 나머지 요소들을 다시 선택 정렬한다.
    selection_sort(arr, start + 1)


arr = [1, 7, 4, 9, 6, 8, 2, 3, 5]
print(arr)

selection_sort(arr, 0)
print(arr)
