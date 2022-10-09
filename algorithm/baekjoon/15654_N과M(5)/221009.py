
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for num in arr:
        if num not in s:
            s.append(num)
            dfs()
            s.pop()


dfs()