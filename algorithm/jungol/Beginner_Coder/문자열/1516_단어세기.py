string = input().split()


while string != ['END']:
    ans = {}
    while string:
        char = string[0]
        num = string.count(char)
        ans[char] = num
        string.remove
        while char in string:
            string.remove(char)
    ans_list = []
    for key, val in ans.items():
        ans_list.append([key, val])

    ans_list.sort()
    for res in ans_list:
        print(res[0], ':', res[1])

    string = input().split()