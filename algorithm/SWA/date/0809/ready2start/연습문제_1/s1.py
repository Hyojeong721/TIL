import sys
sys.stdin = open('input.txt')


# 숫자 입력받기
number = int(input())
result = '홀수' if number % 2 else '짝수'
print(result)

# 1차원 배열 입력받기
numbers = list(map(int, input().split()))
total = 0

for number in numbers:
    total += number

print(total)

# 2차원 배열 입력받기
N = int(input())
board = []

for _ in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)

total_number = 0
for row in board:
    for number in row:
        total_number += number

print(total_number)
