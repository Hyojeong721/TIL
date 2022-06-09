import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    operators = ['-', '+', '*', '/']
    op = [0] * (N+1)
    datum = [[] for _ in range(N+1)]
    for j in range(1, N+1):
        data = list(input().split())
        datum[j] = data
        op[int(data[0])] = data[1]
    for i in range(len(op)-1, 0, -1):
        if op[i] in operators:
            if op[i] == '-':
                op[i] = float(op[int(datum[i][2])]) - float(op[int(datum[i][3])])
            elif op[i] == '+':
                op[i] = float(op[int(datum[i][2])]) + float(op[int(datum[i][3])])
            elif op[i] == '*':
                op[i] = float(op[int(datum[i][2])]) * float(op[int(datum[i][3])])
            elif op[i] == '/':
                op[i] = float(op[int(datum[i][2])]) / float(op[int(datum[i][3])])
    print(f'#{tc} {int(op[1])}')