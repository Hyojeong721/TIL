n = input()
sum = 0
for i in range(len(n)):
    if n[len(n)-i-1] == '1':
        sum += (2 ** i)
    else:
        pass

print(sum)