arr = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []

    def quick_sort(new_arr, left, right):
        if left >= right:
            return

        # 배열의 첫 번째 값을 pivot값으로 정한다.
        pivot = left
        i, j = left + 1, right

        while i <= j:
            # 왼쪽에서 피벗보다 큰 값의 인덱스를 찾는다.
            while i <= j and new_arr[i] <= new_arr[pivot]:
                i += 1

            # 오른쪽에서 피벗보다 작은 값의 인덱스를 찾는다.
            while i <= j and new_arr[j] >= new_arr[pivot]:
                j -= 1

            if i <= j:
                new_arr[i], new_arr[j] = new_arr[j], new_arr[i]

        new_arr[pivot], new_arr[j] = new_arr[j], new_arr[pivot]

        quick_sort(new_arr, left, j - 1)
        quick_sort(new_arr, j + 1, right)

    for c in range(len(commands)):
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]

        new_arr = array[i - 1:j]
        quick_sort(new_arr, 0, len(new_arr) - 1)
        answer.append(new_arr[k-1])

    return answer
print(solution(arr, command))
