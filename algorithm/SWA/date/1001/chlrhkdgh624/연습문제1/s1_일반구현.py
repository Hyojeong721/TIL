# 선택 정렬 함수 구현
import random
random.seed(1234)
numbers = random.sample(range(1, 46), 6)


def selection_sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
        print(f'i={i}', arr)

    return arr

print(numbers)
print(selection_sort(numbers))


