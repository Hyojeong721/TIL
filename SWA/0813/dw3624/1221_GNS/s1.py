import sys
sys.stdin = open('input.txt', encoding = 'utf-8')

T = int(input())

for t in range(1, T + 1):
    t = input().split()[0]
    numbers = list(input().split())
    num_cnt = [0] * 10
    num_alien = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for number in numbers:
        for k in range(len(num_alien)):
            if number == num_alien[k]:
                num_cnt[k] += 1

    result = ''
    for i in range(len(num_alien)):
        for j in range(num_cnt[i]):
            result += '{} '.format(num_alien[i])
    result = result[:-1]

    print(t)
    print(result)