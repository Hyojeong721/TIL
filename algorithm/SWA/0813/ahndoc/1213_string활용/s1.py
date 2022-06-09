import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

T = 10
for tc in range(1, T + 1):
    tc = int(input())
    my_str = input()
    sentence = input()

    cnt = 0
    for i in range(len(sentence)-len(my_str)+1):
        check = 0
        for m in range(len(my_str)):
            if my_str[m] == sentence[i+m]:
                check += 1
            if check == len(my_str):
                cnt += 1
    print('#{} {}'.format(tc, cnt))




