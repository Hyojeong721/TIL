import sys
sys.stdin = open('input.txt')

T = int(input())


def triplet(a):
    tri = {}
    for i in range(len(a)):
        tri[a[i]] = tri.get(a[i], 0) + 1
        if tri[a[i]] >= 3:
            return 1
    return 0


def run_game(a):
    for i in range(len(a)):
        if a[i] - 2 in a and a[i] - 1 in a:
            return 1
    return 0


for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    p1 = []
    p2 = []
    answer = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            p1.append(lst[i])
        else:
            p2.append(lst[i])

        if i >= 4 and answer == 0:
            if triplet(p1) or run_game(p1):
                answer = 1

            if triplet(p2) or run_game(p2):
                if answer == 1:
                    answer = 0
                else:
                    answer = 2
                break

    print('#{} {}'.format(tc, answer))
