import sys
sys.stdin = open('input.txt')

T = int(input())
key_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(1, T+1):
    TC, str_num = input().split()
    str_num = int(str_num)
    print(TC)
    search_str = input()
    for n in range(10):
        key_len = len(key_str[n])
        i = 0
        j = 0
        while len(search_str) > i and key_len > j:
            if search_str[i] != key_str[n][j]:
                i = i - j
                j = -1
            i += 1
            j += 1
            if j == key_len:
                print(key_str[n], end=' ')
                j = 0
        print()
