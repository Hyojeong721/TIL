import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    # print(pascal(n))
    lst = []

    for i in range(1, n+1):
        for j in range(1, i+1):
            lst2 = [1] * j
        lst.append(lst2)
        lst2 = []

    for i in range(2, n):
        for j in range(len(lst[i])):
            if j-1 in range(len(lst[i-1])) and j in range(len(lst[i-1])):
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    print('#{}'.format(tc))
    for i in range(n):
        print(' '.join(list(map(str, lst[i]))))