import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    count = [0] * 10
    N = int(input())
    numbers = input()
    max_num = 0
    max_count = 0

    for num in numbers:
        count[int(num)] += 1

    for idx, cnt in enumerate(count):
        if cnt > max_count:
            max_count = cnt
            max_num = idx
        elif cnt == max_count:
            if idx > max_num:
                max_num = idx

    print("#{0} {1} {2}".format(tc, max_num, max_count))
