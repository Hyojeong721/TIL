import sys

sys.stdin = open('input.txt')

T = int(input())

total = []
numbers = []

for i in range(T):
    total.append(int(input()))
    numbers.append(list(map(int, input())))

for i in range(T):
    count = [0] * 10
    for j in numbers[i]:
        count[j] += 1

    freq_idx = 0
    for idx, x in enumerate(count):
        if x >= count[freq_idx]:
            freq_idx = idx

    print(f'#{i+1} {freq_idx} {count[freq_idx]}')
