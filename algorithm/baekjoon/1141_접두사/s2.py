import sys
sys.stdin = open('input.txt')

n = int(input())
lst = [input() for _ in range(n)]
lst.sort()
excep = lst[:]

for idx, test in enumerate(lst):
    for temp in lst[idx:]:
        if test != temp and test == temp[:len(test)]:
            excep.remove(test)
            break

print(len(set(excep)))
