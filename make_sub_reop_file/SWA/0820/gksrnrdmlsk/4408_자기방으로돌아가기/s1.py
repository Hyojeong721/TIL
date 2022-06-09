import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append([(i+1) // 2 for i in list(map(int, input().split()))])
    lst = sorted(lst, key=min)
    sorted_lst = []
    for j in range(N):
        sorted_lst.append([min(lst[j]), max(lst[j])])
    cnt = 0
    students = N
    while students:
        temp = sorted_lst.pop(0)
        students -= 1
        cnt += 1
        if sorted_lst:
            while temp[1] < sorted_lst[-1][0]:
                for idx, value in enumerate(sorted_lst):
                    if value[0] >= temp[1]:
                        temp = sorted_lst.pop(idx)
                        break
                students -= 1
                if not sorted_lst:
                    break
    print('#{} {}'.format(tc, cnt))



