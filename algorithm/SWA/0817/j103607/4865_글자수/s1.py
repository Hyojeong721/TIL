import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    my_dict = dict()
    for s in str2:
        if s in str1:
            value = my_dict.get(s, 0) + 1
            my_dict[s] = value

    maxV = 0
    for value in my_dict.values():
        if value > maxV:
            maxV = value
    print('#{} {}'.format(tc, maxV))