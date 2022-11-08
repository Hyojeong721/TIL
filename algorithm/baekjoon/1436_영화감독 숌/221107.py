import sys
input = sys.stdin.readline

N = int(input())
res = 0
test = 666

while True:
    if res == N:
        break
    if '666' in str(test):
        res += 1
    test += 1

print(test-1)
