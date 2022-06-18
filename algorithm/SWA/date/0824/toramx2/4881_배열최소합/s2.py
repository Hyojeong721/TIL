def permutations(head, tail=''):
    global result
    if len(head) == 0:
        result.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])

result = []
a = range(5)
print(a)
permutations(a)
print(result)