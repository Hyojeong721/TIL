import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):
    case = input()
    word = input()

    text = input()
    cnt = 0
    answer = 0
    for i in range(len(text)):
        if word[cnt] == text[i]:
            cnt += 1
        else:
            if word[0] == text[i]:
                cnt = 1
            else:
                cnt = 0

        if cnt == len(word):
            cnt = 0
            answer += 1

    print(f'#{test_case} {answer}')









