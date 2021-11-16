import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    str1 = input()
    str2 = input()
    set1 = set()

    for i in str1:
        set1.add(i)

    max_num = 0
    for i in set1:
        cnt = 0
        for j in str2:
            if i == j:
               cnt += 1
        if cnt > max_num:
            max_num = cnt

    print(f'#{test_case} {max_num}')
