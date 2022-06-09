import sys
sys.stdin = open('input.txt')

def find(numbers, change):
    """
    :param numbers: 숫자판
    :param change: 현재 교환 횟수
    :return:
    """
    global ans

    if change == C:
        if ans < int(''.join(numbers)):
            ans = int(''.join(numbers))
        return

    else:
        # 중복이 많으므로 여기에서 가지치기 해주자(기억)

        if ''.join(numbers) in visited:
            return
        visited.append(''.join(numbers))

        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                find(numbers, change + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]

T = int(input())
for tc in range(1, T+1):
    numbers, C = input().split()
    C = int(C)
    numbers = list(numbers)
    visited = []
    ans = 0
    find(numbers, 0)
    print('#{} {}'.format(tc, ans))



# for tc in range(1,int(input())+1):
#     data, K = input().split() # 숫자판의 정보, 교환횟수
#     K = int(K)
#     N = len(data)
#     now = set([data])
#     nxt = set()
#     for _ in range(K):
#         while now:
#             s = now.pop()
#             s = list(s)
#             for i in range(N):
#                 for j in range(i+1,N):
#                     s[i],s[j] = s[j],s[i]
#                     nxt.add(''.join(s))
#                     s[i], s[j] = s[j], s[i]
#         now,nxt = nxt,now
#
#     print('#{} {}'.format(tc,max(map(int,now))))

# T = int(input())
# for tc in range(1, T+1):
#     numbers, c = input().split()
#     C = int(c)
#     N = len(numbers)
#     numbers = list(numbers)
#     num_list = []
#
#     for c in range(C):
#         if c >= 1:
#             temp = []
#             for num in num_list:
#                 number = list(num)
#                 for i in range(N):
#                     for j in range(N):
#                         if i != j:
#                             number[i], number[j] = number[j], number[i]
#                             temp.append(''.join(number))
#                             # num_list.append(''.join(number))
#                             number[i], number[j] = number[j], number[i]
#             temp = list(set(temp))
#             num_list = temp
#
#         else:
#             for i in range(N):
#                 for j in range(N):
#                     if i != j:
#                         numbers[i], numbers[j] = numbers[j], numbers[i]
#                         num_list.append(''.join(numbers))
#                         numbers[i], numbers[j] = numbers[j], numbers[i]
#
#             num_list = list(set(num_list))
#
#
#
#     ans = max(map(int, num_list))
#     print('#{} {}'.format(tc, ans))
