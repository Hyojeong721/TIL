import sys
sys.stdin = open('input.txt')

numbers = input()
for i in range(7):
    ans = 0
    for j in numbers[i:i+7]:
        ans += 2 ** int(j)
    print(ans, end=' ')
