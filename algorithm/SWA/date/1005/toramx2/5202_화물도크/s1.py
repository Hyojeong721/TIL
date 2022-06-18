import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    works = sorted(works, key=lambda x: x[1])

    result = 0
    now = 0
    for i in range(N):
        start = works[i][0]
        end = works[i][1]
        if now <= start:
            result += 1
            now = end

    print('#{} {}'.format(test_case, result))


