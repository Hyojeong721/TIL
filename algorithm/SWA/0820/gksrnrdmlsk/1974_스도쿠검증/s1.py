import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = 9
    lst = [list(map(int, input().split())) for _ in range(N)]
    result = 1
    for i in range(N): # 가로 탐색
        if len(set(lst[i])) != 9:
            result = 0
            break

    for r in range(N): # 세로 탐색
        test = set()
        for c in range(N):
            test.add(lst[c][r])
        if len(test) != 9:
            result = 0
            break

    for i in range(3): # 사각형 블록 탐색
        for j in range(3):
            test2 = set()
            for m in range(3):
                for n in range(3):
                    test2.add(lst[3 * i + m][3 * j + n])
            if len(test2) != 9:
                result = 0
                break
    print('#{} {}'.format(tc, result))
