import sys

sys.stdin = open('input.txt')

N = int(input())

lengths = []
numbers = []

for i in range(N):
    cnt = int(input())
    number = list(map(int, input().split()))
    lengths.append(cnt)
    numbers.append(number)

for length, num_list in zip(lengths, numbers):
    for i in range(length-1, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

results = []
for i in range(N):
    diff = numbers[i][lengths[i]-1] - numbers[i][0]
    results.append(diff)


for idx, result in enumerate(results):
    print(f'#{idx+1} {result}')





