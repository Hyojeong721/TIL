import sys
sys.stdin = open('input.txt')

T = int(input())
def find_brute_num(T, P):
    count = 0
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m:
            if T[i+k] != P[k]:
                break
            else:
                k += 1
        if k == m:
            count += 1
    return count

print(find_brute_num('test', 'tt'))
print(find_brute_num('asdfasdfasdfasdfasdfasdf', 'asdfasdf'))


for test_case in range(T):
    A, B = input().split()
    countP = find_brute_num(A, B)
    # newT = A.replace(B, "")


    # print("#{} {}".format(test_case+1, len(newT)+countP))
    result = len(A) - A.count(B) * (len(B) - 1)
    print("#{} {}".format(test_case+1, result))

    ((()()))