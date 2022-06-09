import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    int_a = int("".join(list(reversed(a))))
    int_b = int("".join(list(reversed(b))))
    if int_a > int_b:
        print(int_a)
    else:
        print(int_b)