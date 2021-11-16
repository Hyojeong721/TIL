import sys
sys.stdin = open('input.txt')

number = int(input())
result = '홀수' if number % 2 else '짝수'
print(result)

numbers = list(map(int, input().split()))

total = 0
for number in numbers:
    total += number

print(total)

N = int(input())
total = 0
for num3 in range(N):
    num3 = list(map(int, input().split()))
    for num in num3:
        total += num

print(total)
