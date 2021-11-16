import sys
sys.stdin = open('input.txt')

def longest_palindrome(strings):
    pass



T = int(input())
for test_case in range(1, T + 1):
    strings = [input() for _ in range(100)]
    print('#{} {}'.format(test_case, longest_palindrome(strings)))