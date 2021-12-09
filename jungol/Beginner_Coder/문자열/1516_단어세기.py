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
    print(ans)
    keys = list(ans.keys())
    keys.sort()
    vals = list(ans.values())
    vals.sort()

    print(keys)
    print(vals)

    string = input().split()