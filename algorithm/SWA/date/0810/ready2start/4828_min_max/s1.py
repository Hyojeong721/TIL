import sys
sys.stdin = open('input.txt')


# 배열의 가장 큰 수를 구하는 함수
def get_max(numbers):
    # 초기값 설정
    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number


# 배열의 가장 작은 수를 구하는 함수
def get_min(numbers):
    # 초기값 설정
    min_number = numbers[0]

    for number in numbers:
        if number < min_number:
            min_number = number

    return min_number


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # diff : 가장 큰 수와 가장 작은 수의 차이
    diff = get_max(numbers) - get_min(numbers)
    print("#{0} {1}".format(tc, diff))
