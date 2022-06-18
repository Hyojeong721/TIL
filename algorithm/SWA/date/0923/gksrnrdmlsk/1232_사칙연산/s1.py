import sys
sys.stdin = open('input.txt')

def calc(node):
    global answer
    if len(lst[node]) >= 2:
        if lst[node][0] == '+':
            return calc(lst[node][1]) + calc(lst[node][2])
        elif lst[node][0] == '-':
            return calc(lst[node][1]) - calc(lst[node][2])
        elif lst[node][0] == '*':
            return calc(lst[node][1]) * calc(lst[node][2])
        else:
            return calc(lst[node][1]) / calc(lst[node][2])

    else:
        return int(lst[node][0])


T = 10
for tc in range(1, T + 1):
    answer = 0
    N = int(input())
    lst = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        temp = input().split()
        lst[i].append(temp[1])
        if len(temp) >= 3:
            for j in temp[2:]:
                lst[i].append(int(j))
    answer = int(calc(1))
    print('#{} {}'.format(tc, answer))