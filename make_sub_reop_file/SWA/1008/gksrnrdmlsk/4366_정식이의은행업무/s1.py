import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    bi = input()
    tri = input()
    bi_number = int(bi, 2)
    tri_number = int(tri, 3)
    bi_length = len(bi)
    tri_length = len(tri)
    bi_results = set()
    for i in range(bi_length):
        temp = bi_number + ((int(bi[i]) + 1) % 2 - int(bi[i])) * 2 ** (bi_length - i - 1)
        bi_results.add(temp)

    temp_bi = bi_results.copy()
    tri_results = set()
    for i in range(tri_length):
        temp = tri_number + ((int(tri[i]) + 1) % 3 - int(tri[i])) * 3 ** (tri_length - i - 1)
        temp2 = tri_number + ((int(tri[i]) + 2) % 3 - int(tri[i])) * 3 ** (tri_length - i - 1)
        temp_bi.discard(temp)
        temp_bi.discard(temp2)

    for i in bi_results - temp_bi:
        print('#{} {}'.format(tc, i))