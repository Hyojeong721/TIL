import sys
sys.stdin = open('input.txt')
T = 10


def search(start):
    i = 99
    j = start
    while i > 0:
        i -= 1
        if j > 0 and ladder[i][j-1] == 1:
            while j > 0 and ladder[i][j-1] == 1:
                j -= 1
        elif j < 99 and ladder[i][j+1] == 1:
            while j < 99 and ladder[i][j+1] == 1:
                j += 1

    return j


for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    goal = ladder[-1].index(2)
    print(search(goal))

