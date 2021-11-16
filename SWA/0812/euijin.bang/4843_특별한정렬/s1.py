import sys
sys.stdin = open("input.txt")

T = int(input())

def selectionSort(arr, N):
    """
    선택 정렬을 통해 배열 arr을 오름차순으로 정렬합니다.
    :param arr: 정렬하고자 하는 배열
    :param N: 배열의 길이
    :return: 오름차순으로 정렬된 배열
    """

    for i in range(N-1):
        # 매 정렬시 최소값의 인덱스
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    selectionSort(arr, N)
    print(arr)
    # new_arr : 특별한 정렬을 한 수들을 담은 배열
    new_arr = []

    for i in range(5): # 10개까지 출력
        new_arr.append(arr[N-i-1])
        new_arr.append(arr[i])

    ans = ' '.join(map(str, new_arr))

    print("#{} {}".format(tc,ans))
