'''
미완성
'''

import sys
sys.stdin = open('input.txt')

def isS1inS2(str1, str2):
    """
    보이어-무어 알고리즘을 이용해 문자열 검사.
    str2 문자열에 str1 문자열이 있으면 True, 없으면 False 를 반환하는 함수.

    """
    M = len(str1)
    N = len(str2)
    skip = []
    for i in range(M):
        skip.append(str1[M - 1 - i])

    compare = M - 1
    while compare < N:
        for idx, char in enumerate(skip):
            if str2[compare] == char:
                compare += idx
                break
            elif idx == M - 1:
                compare += M

        if compare >= N:
            return 0

        num_same = 0
        for i in range(M):
            if str2[compare - i] == str1[M - 1 - i]:
                num_same += 1
            else:
                break
        if num_same == M:
            return 1

    return 0

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = isS1inS2(str1, str2)
    print('#{0} {1}'.format(tc, result))