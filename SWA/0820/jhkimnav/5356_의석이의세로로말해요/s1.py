import sys
sys.stdin = open('input.txt')

T = int(input())
for TC in range(1, T+1):
    arr_str = [['-1'] * 15 for _ in range(5)]
    for i in range(5):
        input_str = list(input())
        for j in range(len(input_str)):
            arr_str[i][j] = input_str[j]

    print('#{} '.format(TC), end='')
    for i in range(15):
        for j in range(5):
            if arr_str[j][i] == '-1':
                continue
            else:
                print(arr_str[j][i], end='')
    print()