'''
    문제 시작부에
        "서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다.
        그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다."
    라고 적혀있었기 때문에,

    처음 입력받은 리스트를 sort() 한 후 진행해야 한다..
'''
import sys
sys.stdin = open('input.txt')


def binarysearch(l, r):
    global check, zigzag

    if l > r:
        return

    m = (l + r)//2

    # 왼쪽 탐색 & 직전 탐색이 오른쪽일 경우 실행
    if num < lst[m]:
        if check == 1: return
        check = 1
        binarysearch(l, m-1)

    # 오른쪽 탐색 & 직전 탐색이 왼쪽일 경우 실행
    elif num > lst[m]:
        if check == 2: return
        check = 2
        binarysearch(m+1, r)

    else:
        zigzag += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    lst.sort()

    zigzag = 0
    for num in nums:
        check = 0   # left(1), right(2)
        binarysearch(0, N-1)
    print('#{} {}'.format(tc, zigzag))
