import sys
sys.stdin = open('input.txt')

N = int(input())
words = [input() for _ in range(N)]
res = {}
merge = []
for n in range(N):
    word = words[n].split()
    for idx, unit in enumerate(word):
        if unit[0].lower() not in res:
            word[idx] = '[' + unit[0] + ']' + unit[1:]
            res[unit[0].lower()] = " ".join(word)
            words[n] = res[unit[0].lower()]
            break
    else:
        merge.append(words[n])

while merge:
    temp = merge.pop(0)
    for idx, val in enumerate(temp):
        if val != ' ' and val.lower() not in res:
            res[val.lower()] = temp[:idx] + '[' + temp[idx] + ']' + temp[idx+1:]
            words[words.index(temp)] = res[val.lower()]
            break

for i in words:
    print(i)
