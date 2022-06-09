import sys
sys.stdin = open('input.txt')

# 단일 데이터
number = int(input())
print(number)

result = '홀수' if number % 2 else '짝수'
print(result)

# 여러 데이터
numbers = list(map(int, input().split()))
total = 0

for number in numbers:
    total += number

print(total)

# 입력 개수를 받고, 차례대로 받는 데이터
N = int(input())
print(N)

matrix = []
for i in range(N):
    temp = list(map(int, input().split()))
    matrix.append(temp)

total_number = 0
for row in matrix:
    for number in row:
        total_number += number

print(total_number)