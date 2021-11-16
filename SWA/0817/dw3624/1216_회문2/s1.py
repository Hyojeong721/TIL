import sys
sys.stdin = open('input.txt')


def palindrome_check(row):
    n = m = len(row)
    temp = ''
    cnt = 0

    while m > 0:
        odd = 1 if m % 2 else 0
        for i in range(n-m+1):
            # print(m, i)
            # print(' part1: ', row[i:i+m])
            # print(' part2: ', row[i+m+odd:i+2*m+odd][::-1])
            # print(' all: ', row[i:i+2*m+odd])
            if row[i:i+m] == row[i+m+odd:i+2*m+odd][::-1]:
                temp = row[i:i+2*m+odd]
        if len(temp) > cnt:
            cnt = len(temp)
            print(cnt, temp)
        m -= 1
    return cnt


T = 10

t = int(input())
text = [input() for _ in range(100)]
text_transpose = []
for col in range(len(text)):
    tmp = ''
    for row in range(len(text)):
        tmp += text[row][col]
    text_transpose.append(tmp)


# row1 = text[0][:10]
# print(row1)
# print(row1[:10])
# print(row1[::-1][:10])
# print()

# 가장 긴 회문의 길이 >> 회문이 최대한 길다고 가정 후 시작
# n 줄여나가면서 반복

cnts = []
for i in range(len(text)):
    cnt_temp1 = palindrome_check(text[i])
    cnt_temp2 = palindrome_check(text_transpose[i])
    cnts.extend([cnt_temp1, cnt_temp2])
cnts.sort()
print(cnts[-1])
print(text_transpose)