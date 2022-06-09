# 1213_string 활용

import sys
sys.stdin = open("input.txt", 'r', encoding='UTF8')


T = 10
for tc in range(1, T + 1):
    N = int(input())
    # 찾을 문자열
    search_string = input()
    # 주어진 문장
    given_sentence = input()
    # 결과값
    result = 0
    # 문장에 찾고자 하는 단어가 있는지 확인
    for i in range(len(given_sentence) - len(search_string) + 1):
        for j in range(len(search_string)):
            if given_sentence[i+j] != search_string[j]:
                break
        else:
            result += 1
    print('#{} {}'.format(N, result))
