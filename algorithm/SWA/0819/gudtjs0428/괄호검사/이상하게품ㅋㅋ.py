import sys
sys.stdin = open('input.txt')

# 뻘짓한듯

def if_match(brackets):
    checking = brackets[:]
    i = 1
    while i < len(checking):
        if checking[i] == ')':
            while i >= 0:
               if checking[i-1] == '(':
                   del checking[i], checking[i-1]




T = int(input())
for tc in range(1, T + 1):
    brackets = list(input())
    print()