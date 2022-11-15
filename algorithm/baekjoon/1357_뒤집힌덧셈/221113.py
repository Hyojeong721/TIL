import sys
input = sys.stdin.readline


X, Y = map(int, input().split())



def Rev(x):
    temp = str(x)

    return int(temp[::-1])

print(Rev(Rev(X) + Rev(Y)))