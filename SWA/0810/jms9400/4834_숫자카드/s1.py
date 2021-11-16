import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    n = input()
    numbers = input()
    total = [0] * 10
    max_num = 0
    location = 0


    for num in numbers:
        total[int(num)] += 1

    for idx, value in enumerate(total): #enumerate로 인덱스값 뽑기
        if value >= max_num:
            max_num = value
            location = idx

    print('#{} {} {}'.format(test_case, location, max_num))
