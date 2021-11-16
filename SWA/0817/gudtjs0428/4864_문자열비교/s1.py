import sys
sys.stdin = open('input.txt')

def if_str1_in_str2(str1, str2):
    for i in range(len(str2)-len(str1)+1):
        if str1 == str2[i:i+len(str1)]:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc, if_str1_in_str2(str1, str2)))