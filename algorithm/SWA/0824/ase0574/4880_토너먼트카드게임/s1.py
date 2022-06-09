import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(3):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_list = []
    stack = []

    for index, card in enumerate(arr):
        arr_list.append((index, card))

    # 절반씩 stack에 저장
    stack.append(arr_list[:N//2])
    stack.append(arr_list[(N//2):])

    print(stack)

    # 조건부 행위
    while stack:
        a = stack.pop()
        # 꺼내고도 stack이 남아있고 a가 하나의 수인 경우
        if type(a) == tuple and stack:
            b = stack.pop()
            if type(b) == list:
                stack.append(a)
                stack.append(b)
            # 마지막 가위바위보
            elif len(b) == 2:
                # 가위바위보
                if a[1] < b[1]:
                    stack.append(b)
                elif a[1] == b[1]:
                    if a[0] < b[0]:
                        stack.append(b)
                    else:
                        stack.append(a)
                else:
                    stack.append(a)

        # a에 두 개의 비교대상이 있는 경우
        elif type(a) == list and len(a) == 2:
            print(a)
            # 가위 바위 보 승자
            if a[0][1] < a[1][1]:
                win = a[1]
                print(win)
            elif a[0][1] == a[1][1]:
                if a[0][0] < a[1][0]:
                    win = a[0]
                    print(win)
                else:
                    win = a[0]
                    print(win)
            else:
                win = a[0]
                print(win)

            stack.append(win)

        # 두 개 이상의 비교대상이 있는 경우
        elif len(a) > 2:
            stack.append(a[:len(a)//2])
            stack.append(a[len(a)//2:len(a)+1])
            print(stack)
        else:
            print(a)
            if type(a) == tuple:
                print('#{} {}'.format(tc, a[0]))
            else:
                print('#{} {}'.format(tc, a[0][0]))
            break


