import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N, M = len(str1), len(str2)
    result = []

    for i in range(len(str1)):

