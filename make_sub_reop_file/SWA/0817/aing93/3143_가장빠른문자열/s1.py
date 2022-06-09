import sys
sys.stdin = open('input.txt')

#테스트 케이스 수와 문자열 A, B를 입력받음
T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    len_a = len(a)
    len_b = len(b)
    i = 0
    answer = 0

    # i가 banana 길이보다 작으면
    while i < len_a:
        # a와 b의 첫글자 비교, 만약 같으면
        if a[i] == b[0]:
            # a를 b의 길이만큼 잘라서 b와 일치하는지 확인.
            if a[i:i+len_b] == b:
                # 같다면 입력값 1을 증가, i는 b의 길이만큼 넘어간다
                answer += 1
                i += len_b
            else:
                # 다르면 입력값 1 증가 시키고 i도 1증가시켜 다음 글자 확인
                answer += 1
                i += 1
        else:
            answer += 1
            i += 1
    print('#{} {}'.format(tc,answer))
