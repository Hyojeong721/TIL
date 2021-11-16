import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    n = len(numbers)

    group = []

    #부분집합 만들
    for i in range(1<<n):
        sub_group = []
        for j in range(n):
            if i & (1<<j):
                sub_group.append(numbers[j])
            group.append(sub_group)

    #부분집합의 합 구하기
    result = 0
    for i in range(1<<n):
        total = 0
        for j in range(len(group[i])):
            total += group[i][j]

            if total == 0:
                result += 1
    #부분집합의 합이 0인 부분집합이 존재하는지 확
    if result:
        print(1)

    else:
        print(0)






