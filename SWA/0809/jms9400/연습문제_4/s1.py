import sys
sys.stdin = open('input.txt')

N = int(input())

def babygin(numbers):
    total = [0] * 10
    tri = 0
    run = 0

    for num in numbers:
        total[int(num)] += 1

    for i in range(10):
        if total[i] >= 3:
            total[i] -= 3
            tri += 1

    for i in range(10):
        if total[i] == 1 and i <= 7:
            if total[i+1] == 1 and total[i+2] == 1:
                run += 1

    if run == 1 and tri == 1:
        return tri

for i in range(N):
    numbers = input()
    print(babygin(numbers))