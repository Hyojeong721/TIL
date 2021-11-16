import sys
from collections import deque
sys.stdin = open('input.txt')
AtoF = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

def modifier(word, length):
    dq = deque([])
    stack = [word[-1]]
    for i in range(length * 4 - 2, -1, -1):
        if word[i] != stack[0]:
            dq.append((stack[0], len(stack)))
            stack = [word[i]]
        else:
            stack.append(stack[0])
    return dq


T = int(input())
for tc in range(1, T + 1):
    if tc >= 2:
        break
    answer = ''
    number = ''
    N, M = map(int, input().split())
    for _ in range(N):
        number += input()


    for value in number:
        try:
            if value == '0':
                answer += '0000'
                continue
            result = AtoF[value]
        except:
            result = int(value)

        answer += '0' * (4 - len(bin(result)[2:])) + bin(result)[2:]

    # dq = modifier(answer, N * M)
    # dq.popleft()
    # numbers = set()
    # while dq:
    #     candidates =



    print(tc, modifier(answer, N * M))

