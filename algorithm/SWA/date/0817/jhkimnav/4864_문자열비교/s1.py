import sys
sys.stdin = open('input.txt')


T = int(input())

for TC in range(1, T+1):
    answer = 0
    key_str = input()
    search_str = input()
    if search_str.count(key_str) > 0:
        answer = 1
    else:
        answer = 0

    print('#{} {}'.format(TC, answer))