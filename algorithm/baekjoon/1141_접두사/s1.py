import sys
sys.stdin = open('input.txt')
# 시간 초과
import itertools

n = int(input())
words = [input() for _ in range(n)]
res = 0
words.sort()
for i in range(n+1, 0, -1):
    for temp in itertools.combinations(words, i):
        temp = list(temp)
        temp.sort()

        for idx, tem in enumerate(temp):
            test = False
            for id, k in enumerate(temp):
                if idx != id and tem == k:
                    test = True
                    break
                if tem != k and len(tem) <= len(k):
                    if tem == k[:len(tem)]:
                        # print(tem, k, k[:len(tem)])
                        test = True
                        break
            if test:
                break

        if not test:
            res = max(res, len(temp))
            break

    if res != 0:
        break

print(res)