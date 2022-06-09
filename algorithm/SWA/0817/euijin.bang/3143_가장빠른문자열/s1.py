import sys
sys.stdin = open('input.txt')

Testcase = int(input())

def find_brute_num(T, P):
    count = 0
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m:
            count += 1
    return count

for test_case in range(Testcase):
    T, P = input().split()
    countP = find_brute_num(T, P)
    newT = T.replace(P, "")
    print(newT)
    print("#{} {}".format(test_case+1, len(newT)+countP))
