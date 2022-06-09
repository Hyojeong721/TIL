import sys
sys.stdin = open('input.txt')

def selection_sort(N, numbers):
    """
    최댓값, 최솟값 순서로 선택 정렬하는 함수
    N: 정수의 개수
    numbers: 정렬할 정수 리스트

    """
    for i in range(N):
        if i % 2:
            min = -1
            for j in range(i, N):
                if numbers[min] > numbers[j]:
                    min = j
            numbers[i], numbers[min] = numbers[min], numbers[i]
        else:
            max = -1
            for j in range(i, N):
                if numbers[max] < numbers[j]:
                    max = j
            numbers[i], numbers[max] = numbers[max], numbers[i]

    return numbers

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    sorted_numbers = selection_sort(N, numbers)
    result = ''
    for i in range(10):
        result += str(sorted_numbers[i])
        result += ' '
    print('#{0} {1}'.format(tc, result))