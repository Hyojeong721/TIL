import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())
    Data = list(map(int, input().split()))

    result = []
    for i in range(N-M+1):
        result.append(sum(Data[i:i+M]))

    print('#%s %d'%(T, max(result)-min(result)))