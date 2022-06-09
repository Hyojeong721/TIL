T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    str_dict = {}
    for s1 in str1:
        if s1 in str2:
            str_dict[s1] = str2.count(s1)

    max_v = 0
    for v in str_dict.values():
        if v > max_v:
            max_v = v

    print('#{} {}'.format(tc, max_v))