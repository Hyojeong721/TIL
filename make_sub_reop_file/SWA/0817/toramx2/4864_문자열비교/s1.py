import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    i = 0
    j = 0
    result = 0

    # Brute Force
    while i < N and j < M:
        if str2[j] != str1[i]:
            j = j - i
            i = -1
        i += 1
        j += 1

    if i == N:      # 모든 글자가 일치했을때
        result = 1

    print('#{0} {1}'.format(test_case, result))