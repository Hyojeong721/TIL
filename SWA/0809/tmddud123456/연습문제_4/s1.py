import sys
sys.stdin = open('input.txt')


def define_triple(list_number):
    return_number = 0
    for i in range(0, len(list_number)):
        if list_number[i] == 6:
            return_number += 2
        if list_number[i] == 3:
            list_number[i] -= 3
            return_number += 1
    return return_number

def define_run(list_number):
    return_number = 0
    for i in range(1, len(list_number) - 1):
        if list_number[i-1] == list_number[i] == list_number[i + 1] >= 1:
            if list_number[i] == 2:
                return_number += 1
                list_number[i - 1] -= 1
                list_number[i] -= 1
                list_number[i + 1] -= 1
            list_number[i - 1] -= 1
            list_number[i] -= 1
            list_number[i + 1] -= 1
            return_number += 1

    return return_number

test_case = int(input())
for tc in range(test_case):
    baby_gin_check = 0
    define_baby_gin = list(map(int, input()))
    # 0~9까지의 값 저장
    count_number = [0] * 10
    for i in define_baby_gin:
        count_number[i] += 1
    baby_gin_check = define_triple(count_number)
    baby_gin_check = baby_gin_check + define_run(count_number)
    if baby_gin_check == 2:
        print('it is babygin')
    else:
        print('it it not babygin')


