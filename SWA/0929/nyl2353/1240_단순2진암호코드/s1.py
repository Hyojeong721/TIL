import sys
sys.stdin = open('input.txt')


codes = ['0001101', '0011001', '0010011', '0111101',
         '0100011', '0110001', '0101111', '0111011',
         '0110111', '0001011']


def findpw(arr, row, col):
    """
    arr 배열의 [row, col]에서 시작하는 암호코드가 있는지 검사

    Returns:
        (암호코드가 있는 경우) True, 암호 list(8개의 숫자)
        (암호코드가 없는 경우) False, 0

    """
    pw = []
    r = row
    c = col

    # 1번째 줄 암호 8자리 완성
    while True:
        digit = arr[r][c:c+7]

        if digit not in codes:
            return False, 0
        else:
            idx = codes.index(digit)
            pw.append(idx)
            c += 7

        if len(pw) == 8:
            break

    # 2~5번째 줄 암호 검사
    for r in range(row+1, row+5):
        for c in range(8):
            if arr[r][col+7*c:col+7*c+7] != codes[pw[c]]:
                return False, 0

    return True, pw


def is_cypher(lst):
    """
    암호코드가 정상적인지 검사

    Returns:
        (유효한 경우) 암호코드의 합(int)
        (유효하지 않은 경우) 0

    """
    total = 0

    for i in range(8):
        if i % 2:
            total += lst[i]
        else:
            total += lst[i] * 3

    if total % 10 == 0:
        return sum(lst)
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    r, c = 0, 0
    while r < N:
        # 행에 1이 없으면 다음 행으로 넘어감
        if '1' not in arr[r]:
            r += 1
        # c부터 끝 열까지의 길이가 암호코드 길이보다 짧으면 다음 행으로 넘어감
        if 56 > M - c:
            c = 0
            r += 1

        # 암호 찾으면 break, 못찾으면 다음 열로 넘어감
        if int(arr[r][c+6]):
            is_correct, ans = findpw(arr, r, c)
            if is_correct:
                break
            else:
                c += 1
        else:
            c += 1

    print('#{} {}'.format(tc, is_cypher(ans)))

