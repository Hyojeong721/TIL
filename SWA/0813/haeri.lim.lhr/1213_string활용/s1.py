import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

T = 10

def count(char, sentence):

    result = 0
    for i in char:
        for j in sentence:
            if i == j:
              for k in range(len(char)):
                  if char[char.index(i) + k] != sentence[sentence.index(j) + k]:
                      break




    return result

for test_case in range(1, T+1):
    N = input()
    char = input()
    sentence = input()

    print('#%d %d' %(test_case, count(char,sentence)))