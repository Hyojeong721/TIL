# 1221 GNS

import sys
sys.stdin = open("input.txt", 'r', encoding='UTF8')

# 첫 줄의 테스트 케이스를 받아온다.
T = int(input())
# print(T) = 10개
accurate_word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(T):
    numbers, data = input().split()
    string_list = list(input().split())
    print(string_list)
    # print(string_list) string_list는 svn,for,zro 등의 데이터를 포함
    target_dict = []
    for i in range(T):
        for string in string_list:
            if accurate_word[i] == string:
                target_dict.append(string)

    print(numbers)
    print(*target_dict)





