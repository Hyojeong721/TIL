import sys
sys.stdin = open('input.txt')

def create_password(q):
    i = [1, 2, 3, 4, 5]
    while q[0] - i[0] > 0:
        q.append(q.pop(0) - i[0])
        i.append(i.pop(0))
    q.pop(0)
    q.append(0)
    return q

T = 10
for test_case in range(1, T + 1):
    input()
    q = list(map(int, input().split()))
    print('#{}'.format(test_case), end=' ')
    for p in create_password(q):
        print(p, end=' ')
    print()