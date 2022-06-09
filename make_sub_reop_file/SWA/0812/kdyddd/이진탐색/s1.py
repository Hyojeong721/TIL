import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    input_text = list(map(int, input().split()))

    A = input_text[1]
    B = input_text[2]

    min_page_a = 1
    max_page_a = input_text[0]
    page_a = (min_page_a + max_page_a) // 2

    min_page_b = 1
    max_page_b = input_text[0]
    page_b = (min_page_b + max_page_b) // 2

    while page_a != A and page_b != B:
        if page_a < A:
            min_page_a = page_a
        else:
            max_page_a = page_a
        page_a = (min_page_a + max_page_a) // 2

        if page_b < B:
            min_page_b = page_b
        else:
            max_page_b = page_b
        page_b = (min_page_b + max_page_b) // 2

    if page_a == A and page_b == B:
        print(f'#{test_case} 0')
    elif page_a == A:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} B')