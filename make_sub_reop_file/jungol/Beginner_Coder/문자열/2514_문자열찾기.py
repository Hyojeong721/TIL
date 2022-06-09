string = input()
koi_cnt = 0
ioi_cnt = 0

for idx, char in enumerate(string):
    if char == 'K':
        if idx+2 < len(string):
            if string[idx+1] == 'O' and string[idx+2]=='I':
                koi_cnt += 1
    elif char == 'I':
        if idx+2 < len(string):
            if string[idx+1] == 'O' and string[idx+2]=='I':
                ioi_cnt += 1

print(koi_cnt)
print(ioi_cnt)