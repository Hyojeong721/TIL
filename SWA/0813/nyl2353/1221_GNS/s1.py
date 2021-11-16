import sys
sys.stdin = open('input.txt')

def digit_sort(len, chars):
    """
    선택 정렬을 통해 문자열 숫자를 올림차순으로 정렬하는 함수
    len: 문자열 숫자 개수
    chars: 문자열 숫자 리스트

    """
    digits = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # 선택 시작점
    start = 0
    #
    for digit in digits:
        for i in range(start, len):
            if chars[i] == digit:
                chars[i], chars[start] = chars[start], chars[i]
                start += 1

    return chars

T = int(input())
for _ in range(T):
    case, len = input().split()
    chars = input().split()
    sorted = digit_sort(int(len), chars)
    sorted = ' '.join(sorted)
    print(case)
    print(sorted)