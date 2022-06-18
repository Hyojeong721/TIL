import sys
sys.stdin = open('input.txt')

# test case 개수
T = int(input())

# 각 test case 별로 진행
for t in range(1, T + 1):
    # 양수의 개수
    N = int(input())
    # N개의 양수의 list
    lst_a = list(map(int, input().split()))

    # list 에서 minimum 과 maximum 구함
    minimum = lst_a[0]
    maximum = lst_a[0]
    for a in lst_a:
        if a < minimum:
            minimum = a
        if a > maximum:
            maximum = a

    # 차이를 구하고 test case 번호와 함께 출력
    diff = maximum - minimum
    print('#{0} {1}'.format(t, diff))