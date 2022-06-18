import sys
sys.stdin = open('input.txt')

# 민선이 방법처럼 stack에 넣고 같다면 stack에서 지우고 아니면 추가하는게 더 효율적인듯

def delete_duple(string):
    new_string = string
    i = 0
    while i < len(new_string) - 1:
        if new_string[i] == new_string[i+1]:
            new_string = new_string[:i] + new_string[i+2:]
            i = 0
        else:
            i += 1
    return len(new_string)


T = int(input())
for tc in range(1, T + 1):
    string = input()
    print('#{} {}'.format(tc, delete_duple(string)))