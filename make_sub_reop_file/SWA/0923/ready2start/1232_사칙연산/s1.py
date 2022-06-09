import sys
sys.stdin = open('input.txt')


# 유효한 값이 들어온다고 가정하고 예외 처리는 하지 않음.
def operate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 // num2


def calculate_tree(num):
    """
    주어진 노드를 루트 노드로 하는 사칙연산 트리의 값을 구한다.
    Args:
        num: 현재 탐색중인 노드의 번호 (int)
    """
    cnt = nodes[num]

    # 해당 노드가 단말 노드라면 => 숫자 반환
    if not left[num]:
        return int(cnt)

    # 해당 노드가 단말 노드가 아니라면 => 계산값 반환
    left_child = calculate_tree(left[num])
    right_child = calculate_tree(right[num])
    return operate(left_child, cnt, right_child)


T = 10

for tc in range(1, T + 1):
    N = int(input())

    nodes = [-1] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        node, value, *child = input().split()
        nodes[int(node)] = value

        # 해당 노드의 자식 노드가 있다면
        if child:
            left[int(node)] = int(child[0])
            right[int(node)] = int(child[1])

    result = calculate_tree(1)
    print("#{} {}".format(tc, result))
