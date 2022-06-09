import sys
sys.stdin = open('input.txt')

T = int(input())
text = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1):
    case = input().split()
    case_number = case[0]
    N = int(case[1])
    arr = input().split()
    print(arr)

    for i in range(N):
        for j in range(arr):
            if text[i] == arr[j]:
                text[i] = j





