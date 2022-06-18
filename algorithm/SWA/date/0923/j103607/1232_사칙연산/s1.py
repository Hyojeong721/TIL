import sys
sys.stdin = open('input.txt')



def expression(num):

    global result
    if num <= N:
        expression(num*2)
        expression(num*2+1)
        result.append(temp[num])
        if temp[num] == '+':
            return int(temp[-2]) + int(temp[-1])
        elif temp[num] == '-':
            return int(temp[-2]) - int(temp[-1])
        elif temp[num] == '*':
            return int(temp[-2]) * int(temp[-1])
        elif temp[num] == '/':
            return int(temp[-2]) / int(temp[-1])
        else:
            return


#
T = 10
for tc in range(1, T+1):
    N = int(input())   # 노드 총 개수

    temp = [0] * (N+1)
    for i in range(N):
        info = input().split()
        temp[int(info[0])] = info[1]

    result = []
    expression(1)
    print()
