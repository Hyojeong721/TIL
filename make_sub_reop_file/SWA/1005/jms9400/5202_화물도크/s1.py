import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    time_dict = {}

    for i in lst:
        if i[0] in time_dict:
            if time_dict[i[0]] >= i[1]:
                time_dict[i[0]] = i[1]
        else:
            time_dict[i[0]] = i[1]

    answer = 0
    idx = 0
    while idx <= 24:
        if idx in time_dict:
            a = idx
            b = time_dict[a]
            for i in range(a, b):
                if time_dict.get(i, 24) < b:
                    b = time_dict[i]
            idx = b
            answer += 1
        else:
            idx += 1


    print('#{} {}'.format(tc, answer))
