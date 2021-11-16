import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):
    N = int(input())
    line = [[0]]
    for i in range(N):
        line.append(list(input().split()))

    for i in range(len(line)-1, 0, -1):
        if len(line[i]) == 4:
            a = int(line[i][2])
            b = int(line[i][3])
            if line[i][1] == '+':
                line[i][1] = float(line[a][1]) + float(line[b][1])
            elif line[i][1] == '-':
                line[i][1] = float(line[a][1]) - float(line[b][1])
            elif line[i][1] == '*':
                line[i][1] = float(line[a][1]) * float(line[b][1])
            else:
                line[i][1] = float(line[a][1]) / float(line[b][1])

    print('#{} {}'.format(test_case, int(line[1][1])))