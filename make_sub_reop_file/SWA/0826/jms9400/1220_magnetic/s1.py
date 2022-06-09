import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        stack = []
        for j in range(N):
            if arr[j][i] == 1:
                stack.append(1)
            elif arr[j][i] == 2:
                if len(stack):  # stack이 비어있지 않을 때 (비어있으면 버림)
                    if stack[-1] == 1:  # 스택에 1이 있으면 교착상태 발생
                        result += 1
                stack.append(2)
    print('#{} {}'.format(tc, result))