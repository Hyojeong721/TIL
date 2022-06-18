import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    text = list(input())

    for i in range(len(text)):
        for j in range(len(text) - 1):
            if text[j] == text[j + 1]:
                text.pop(j)
                text.pop(j)
                break
    print('#{0} {1}'.format(test_case, len(text)))