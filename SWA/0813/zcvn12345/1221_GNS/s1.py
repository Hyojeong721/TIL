import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    test_case, number_count = input().split()
    numbers = input().split()
    str_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = [0] * 10

    for number in numbers:
        for i in range(10):
            if number == str_numbers[i]:
                result[i] += 1

    result_string = ''
    for i in range(10):
        result_string += (str_numbers[i] + ' ') * result[i]

    print(result_string)