import sys
sys.stdin = open('input.txt')

TC = int(input())


def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)
    for i in range(n - m + 1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1


for test_case in range(TC):
    str1 = input()
    str2 = input()

    T = str2
    P = str1

    P_idx = find_brute(T, P)

    if P_idx == -1:
        result = 0
    else:
        result = 1

    print("#{} {}".format(test_case + 1, P_idx))