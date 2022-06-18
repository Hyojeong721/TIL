# 테스트 케이스 오류 발생 (5/10)
import sys
sys.stdin = open('input.txt')
T = int(input())


def winner(person1, person2):
    a = person1[0]
    b = person2[0]
    if a == b:
        return person1
    elif a == 1 and b == 3:
        return person1
    elif a == 2 and b == 1:
        return person1
    elif a == 3 and b == 2:
        return person1
    else:
        return person2


def div(num):
    if num % 2 == 0:
        return num//2
    else:
        return num//2 + 1


def compete(people):
    stack = []

    M = len(people)
    if M == 1:
        return people[0]

    if M == 2:
        return winner(people[0], people[1])

    group1 = people[0: div(M)]
    group2 = people[div(M):]

    for i in range(div(len(group1))):
        if 2*i+1 <= len(group1) - 1:
            stack.append(winner(group1[2*i], group1[2*i+1]))
        else:
            stack.append(group1[2*i])

    for j in range(div(len(group2))):
        if 2*j+1 <= len(group2) - 1:
            stack.append(winner(group2[2*j], group2[2*j+1]))
        else:
            stack.append(group2[2*j])

    print(stack)

    return compete(stack)


for tc in range(1, T+1):
    N = int(input())
    info = list(map(int, input().split()))
    index = list(range(1, N+1))
    students = list(zip(info, index))
    result = compete(students)[1]
    print(f'#{tc} {result}')



