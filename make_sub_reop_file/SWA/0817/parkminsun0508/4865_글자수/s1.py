import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    str_first = input()
    str_second = input()
    str_dic = {}
    for s in str_first:
        str_dic[s] = 0
    for s in str_second:
        if s in str_dic:
            str_dic[s] += 1

    max_value = 0
    for i, j in str_dic.items():
        if j > max_value:
            max_value = j

    print("#{} {}".format(tc, max_value))