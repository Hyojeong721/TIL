import sys
sys.stdin = open('input.txt', 'r')

hex_str = input()
bin_str = ''
dic = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

for c in hex_str:
    bin_str += format(int(c, 16), 'b').zfill(4)

for key, value in dic.items():
    if key in bin_str:
        print(value, end=', ')


# print("2".zfill(4))
# 0002