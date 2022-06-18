import sys
sys.stdin = open('input.txt')


for i in range(1,11):
    tc_num = int(input())
    chrs = input()
    sentence = input()
    M = len(chrs)
    N = len(sentence)
    cnt = 0
    i = 0
    j = 0

    while i < M and j < N:
        if chrs[i] != sentence[j]:
            j += 1

        else:
            for k in range(len(chrs)):
                if chrs[i + k] != sentence[j + k]:
                    j += 1
                    continue
                else:
                    cnt += 1
    print(cnt)







