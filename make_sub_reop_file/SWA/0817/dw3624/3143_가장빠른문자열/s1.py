import sys
sys.stdin = open('input.txt')

T = int(input())

# a를 한글자씩 확인, b의 첫글자와 일치하는 문자 있는 경우, b의 길이만큼의 인덱스를 확인
for t in range(1, T + 1):
    a, b = input().split()
    cnt = 0
    n = len(b)
    idx = 0

    while idx < len(a):
        if a[idx] == b[0]:
            if a[idx:idx + n] == b:
                idx += n - 1
        cnt += 1
        idx += 1

    print('#{} {}'.format(t, cnt))