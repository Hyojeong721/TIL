import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for tc in range(1, 11):
    n = int(input())
    target = input()
    words = input()
    result = 0
    t = 0 # target
    w = 0 # words

    while t < len(target) and w < len(words):
        if target[t] != words[w]:
            w = w - t
            t = -1
        elif target[t] == words[w] and t == len(target) - 1:
            result += 1
            t = -1
        t += 1
        w += 1


    print('#{} {}'.format(n, result))