import sys
sys.stdin = open('input.txt')

def binary_search(P, key):
    is_answer = False
    search_cnt = 0

    start = 1
    end = P
    Key = key

    while start <= end:
        center = (start + end) // 2
        search_cnt += 1
        if center == Key:
            is_answer = True
            break
        elif center < Key:
            start = center
        else:
            end = center

    return is_answer, search_cnt


T = int(input())
for test_case in range(1, T+1):
    # P : 책의 전체 쪽수
    # Pa : A가 찾을 쪽 번호
    # Pb : B가 찾을 쪽 번호
    P, Pa, Pb = list(map(int, input().split()))
    a_answer, a_search_cnt = binary_search(P, Pa)
    b_answer, b_search_cnt = binary_search(P, Pb)

    if a_answer * a_search_cnt < b_answer * b_search_cnt:
        answer = 'A'
    elif a_answer * a_search_cnt > b_answer * b_search_cnt:
        answer = 'B'
    else:
        answer = 0

    print('#{} {}'.format(test_case, answer))