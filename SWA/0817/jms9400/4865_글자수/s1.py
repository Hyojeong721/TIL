import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    my_dict = {}

    for i in str2:
        if i in str1:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

    result = 0
    for val in my_dict.values():
        if val > result:
            result = val
    print('#{} {}'.format(tc, result))