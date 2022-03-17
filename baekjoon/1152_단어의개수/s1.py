import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    sentence = input().split()
    print(len(sentence))
