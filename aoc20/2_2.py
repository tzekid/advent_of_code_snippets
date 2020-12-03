import re

inputA = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".split('\n')

inputA = open('input2_1.txt').read().split('\n')

passwds = []
for line in inputA:
    r = re.search('(\d{1,})-(\d{1,}) (\w): (\w*)', line)
    if not r:
        continue
    _, low, high, char, string = r[0], int(r[1]), int(r[2]), r[3], r[4]
    # count = re.findall(char, string)
    # if low <= len(count) <= high:
        # passwds.append(string)

    low -= 1
    high -= 1

    first_true = string[low] == char
    second_true = string[high] == char

    if first_true ^ second_true:
        passwds.append(string)

print(len(passwds))
