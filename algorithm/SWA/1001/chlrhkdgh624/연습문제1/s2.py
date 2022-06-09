# 선택 정렬 함수 구현(재귀)
import random
random.seed(1234)
numbers = random.sample(range(1, 46), 6)


def selection_sort(arr, k=0):
    if k == len(arr):
        return arr
    else:
        min_idx = k
        for j in range(k+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[k], arr[min_idx] = arr[min_idx], arr[k]
        return selection_sort(arr, k+1)


# min() 내장함수를 사용할 수 있는 경우
def selection_sort2(arr):
    if len(arr):
        x = min(arr)
        arr.remove(x)
        return [x] + selection_sort2(arr)
    else:
        return []


print(selection_sort(numbers))
print(selection_sort2(numbers))