import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 첫 번째 줄은 항상 숫자 1이기 때문에 시작은 [1]
    pas = [1]
    result = [[1]]
    # result의 길이가 N이하일 때까지만 반복하도록하여 원하는 깊이만큼 결과 출력
    while len(result) < N:
        # 다음 층을 만들어 낼 임시 리스트
        temp = [0]
        # 다음층을 만들기 위해 현재층 길이만큼 for문을 돌림
        for i in range(len(pas)):
            # 파스칼의 삼각형의 규칙은 위의 왼쪽과 오른쪽 숫자의 합
            # 왼쪽 숫자는 append로 깔아주고 오른쪽 숫자는 +로 더해준다.
            temp.append(pas[i])
            temp[i] += pas[i]
        # result의 새로운 층을 추가하고 pas에 새로운층을 덮어 현재층으로 만들어준다.
        result.append(temp)
        pas = temp
    print ('#{}'.format(tc))
    for i in result:
        for j in i:
            print(j, end=' ')
        print()