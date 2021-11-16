import sys
sys.stdin = open('input.txt')

T = int(input())

def abba_check(text):
    for text_row in text:
        for i in range(m_half, len(text_row) + 1):
            temp = text_row[i - m_half:i]

            # 문자열 길이가 홀수인 경우
            if m % 2:
                temp2 = text_row[i + m_half:i:-1]
                if temp == temp2:
                    return text_row[i - m_half:i + m_half + 1]

            # 문자열 길이가 짝수인 경우
            else:
                temp2 = text_row[i+m_half-1:i-1:-1]
                if temp == temp2:
                    return text_row[i - m_half:i + m_half]

for t in range(1, T + 1):
    n, m = map(int, input().split())
    m_half = m // 2
    text = [input() for _ in range(n)]       # 가로줄 검사용
    text_t = []     # 세로줄 검사용
    for col in range(len(text)):
        tmp = ''
        for row in range(len(text)):
            tmp += text[row][col]
        text_t.append(tmp)

    a1 = abba_check(text)
    a2 = abba_check(text_t)

    if a1:
        print('#{} {}'.format(t, a1))
    elif a2:
        print('#{} {}'.format(t, a2))