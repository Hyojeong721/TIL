import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    str1, str2 = input(), input()
    print("#{} {}".format(tc, int(str1 in str2)))
