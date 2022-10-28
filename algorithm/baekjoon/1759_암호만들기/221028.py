# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열
L, C = map(int, input().split())
arr = sorted(list(input().split()))
mo = ['a', 'e', 'i', 'o', 'u']
res = []


def check():
    m, j = 0, 0
    for k in res:
        if k in mo:
            m+=1
        else:
            j+=1
    if m>=1 and j>=2:
        temp = "".join(res)

        print(temp)


def dfs(cnt, idx):
    if cnt == L:
        check()
        return

    for i in range(idx, C):
        res.append(arr[i])
        dfs(cnt+1, i+1)
        res.pop()

dfs(0, 0)



