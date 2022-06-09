import sys
sys.stdin = open('input.txt')

numbers = input()
answer = []
for i in range(len(numbers) // 7):
    result = 0
    for j in range(7):
        if numbers[7 * i + j] == '0':
            pass
        else:
            result += 2 ** (6 - j)

    answer.append(result)

print(answer)
