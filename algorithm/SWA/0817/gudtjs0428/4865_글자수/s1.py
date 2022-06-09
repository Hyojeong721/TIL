import sys
sys.stdin = open('input.txt')

def most_char_in_str(str1, str2):
    pass
    set1 = set(str1)
    char_in_str2 = {}
    for char in set1:
        char_in_str2[char] = str2.count(char)

    max_num = 0
    for value in char_in_str2.values():
        if value > max_num:
            max_num = value
    return max_num


T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc, most_char_in_str(str1, str2)))