import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    counter = []

    for char1 in str1:
        count = 0
        for char2 in str2:
            if char1 == char2:
                count += 1
        counter.append(count)

    print('#{0} {1}'.format(test_case, max(counter)))