import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []

for _ in range(N):
    word = str(input())
    s_word = word.split(" ")
    for i in range(len(s_word)):
        if (s_word[i] != "" and s_word[i][0].upper() not in arr):
            arr.append(s_word[i][0].upper())
            s_word[i] = "[" + s_word[i][0] + "]" + s_word[i][1:]
            s_word = " ".join(s_word)
            print(s_word)
            break
    else:
        for j in range(len(word)):
            if (word[j].isalpha() and word[j].upper() not in arr):
                arr.append(word[j].upper())
                word = word[:j] + "[" + word[j] + "]" + word[j + 1:]
                print(word)
                break
        else:
            print(word)