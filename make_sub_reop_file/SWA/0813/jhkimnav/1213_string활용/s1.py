import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    answer = 0
    # 테스트케이스 번호
    TC = int(input())
    # 찾을 문자열
    key_str = input()
    # 검색할 문장
    search_str = input()

    key_str_len = len(key_str)
    search_str_len = len(search_str)
    i = j = 0
    while i < search_str_len and j < key_str_len:
        if search_str[i] != key_str[j]:
            i = i - j
            j = -1

        i += 1
        j += 1
        if j == key_str_len:
            answer += 1
            j = 0
    print('#{} {}'.format(TC, answer))