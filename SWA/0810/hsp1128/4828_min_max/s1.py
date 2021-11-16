import sys
sys.stdin = open("input.txt")

num_cycle = int(input())
i = 0

while i < num_cycle:
    num = int(input())
    num_list = list(map(int, input().split()))
    maximum = num_list[i]
    minimum = num_list[i]

    for j in range(num):
        if num_list[j] > maximum:
            maximum = num_list[j]
        elif num_list[j] < minimum:
            minimum = num_list[j]
    result = maximum - minimum
    print(f"#{i+1} {result}")

    i += 1