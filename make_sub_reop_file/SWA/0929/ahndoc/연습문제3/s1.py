import sys
sys.stdin = open('input.txt')

numbers = input()
secret_patterns = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# numbers = '0DEC'

my_pattern = ''
for num in numbers:
    if num.isdigit():
        n = format(int(num), 'b')

        if len(n) != 4:
            temp = n
            while len(temp) != 4:
                temp = '0' + temp
            n = temp
        my_pattern += n
    else:
        n = format(dic[num], 'b')
        my_pattern += n

cnt = 0
ans = []
while my_pattern:
    if cnt == 2:
        break
    for i in range(len(my_pattern)-5):
        if cnt == 1:
            cnt += 1
            break
        for j in range(10):
            if len(my_pattern) < 6:
                cnt += 1
                break

            if my_pattern[i:i+6] == secret_patterns[j]:
                ans.append(j)
                my_pattern = my_pattern[i+6:]
for i in ans:
    print(i, end=' ')
