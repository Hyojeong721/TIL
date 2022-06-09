import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst_red = []
    lst_blue = []
    for n in range(N):
        lst = list(map(int, input().split()))
        print(lst)
        if lst[-1] == 1:
            lst_red.append(lst)
        else:
            lst_blue.append(lst)

