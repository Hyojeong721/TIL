import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    word = input()
    text = input()
    answer = 0
    for i in range(len(text) - len(word) + 1):
        if text[i] == word[0]:
            temp = 1
            for j in range(len(word)):
                if text[i+j] != word[j]:
                    temp = 0
            if temp == 1:
                answer = 1
                break

    print(f'#{test_case} {answer}')
