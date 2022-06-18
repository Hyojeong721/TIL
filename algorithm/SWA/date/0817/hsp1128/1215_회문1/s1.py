import sys
sys.stdin = open('input.txt')

def num_palindrome(x):
    result = 0
    #가로 찾기
    for i in range(len(x)):
        for j in range(len(x[i])-l+1):
            tmp = ''
            for k in range(l):
                tmp += x[i][j+k]
            if tmp == tmp[::-1]:
                result += 1


    #세로 찾기
    for i in range(len(x)):
        for j in range(len(x)-l+1):
            tmp = ''
            for k in range(l):
                tmp += x[j+k][i]
            if tmp == tmp[::-1]:
                result += 1

    return result

for tc in range(1, 11):
    l = int(input())
    arr = [input() for _ in range(8)]
    print('#{} {}'.format(tc,num_palindrome(arr)))
