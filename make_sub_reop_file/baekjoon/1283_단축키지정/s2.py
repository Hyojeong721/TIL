import sys
sys.stdin = open('input.txt')
# 왜 답이 아닌지 모르겠는데.. 답아님 테케는 통과
N = int(input())
words = [str(input()) for _ in range(N)]
res = set()
for n in words:
    lst = n.split(" ")
    # 단어 첫번째에서 단축키 지정하는 경우
    for idx, word in enumerate(lst):
        if word[0] != "" and word[0].lower() not in res:
            res.add(word[0].lower())
            lst[idx] = '[' + word[0] + ']' + word[1:]
            print(" ".join(lst))
            break
    # 단어 첫번째에서 지정 안 된 경우
    else:
        check = True
        for idx, word in enumerate(lst):
            if check:
                for ix, i in enumerate(word):
                    if i.isalpha() and i.lower() not in res:
                        res.add(i.lower())
                        lst[idx] = word[:ix] + '[' + word[ix] + ']' + word[ix+1:]
                        print(*lst)
                        check = False
                        break
                else:
                    print(*lst)
                    break
            else:
                break
