#문제 잘못 이해함
# 무조건 2개씩이 아니라 N//2개씩임!
import sys
sys.stdin = open('input.txt')


def search(index):
    global arr, min_sub, N, first, second

    for i in range(len(first)):
        if i not in index[:N//2]:
            first = index[:N//2]
            second = index[N//2:]
            print(comb(len(first),2,0,0))

    print('first', first)

    # if min_sub >= abs(a-b):
    #     min_sub = abs(a-b)

    return

# 순열
def permute(nums):

    prev_elements = []

    def dfs(elements):

        if len(elements) == 0:
            search(prev_elements)



        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return



# 조합
def com(n, r, s, k):

    if k == r:
        return comb

    else:
        for i in range(s,n-r+k+1):
            comb[k]=i
            com(n, r, i+1, k+1)



T = int(input())

for tc in range(1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    comb = [0] * N
    min_sub = 999999
    first = []
    second = []
    permute(com(N, N, 0, 0))


    print("#{} {}".format(tc, min_sub))
