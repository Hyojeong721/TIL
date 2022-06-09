str_arr = [input() for _ in range(5)]

# max 길이 찾기
max_len = 0
for i in range(5):
    if len(str_arr[i]) > max_len:
        max_len = len(str_arr[i])

ans = ''
for j in range(max_len):
    for i in range(5):
        if len(str_arr[i]) <= j:
            pass
        else:
            ans = ans + str_arr[i][j]

print(ans)