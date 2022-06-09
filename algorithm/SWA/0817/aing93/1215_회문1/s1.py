import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    length = int(input())

    str_table = []
    for _ in range(8):
        str_table.append(input())

    count = 0

    for i in range(8):
        for j in range(8-length+1):
