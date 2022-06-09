string = input().split()
ans = []
while string != ['END']:
    for i in string:
        if i not in ans:
            ans.append(i)

    print(*ans)
    string = input().split()
