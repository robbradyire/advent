codes = open("input.txt").read().strip().split("\n")

for i, code in enumerate(codes):
    for other_code in codes[i + 1:]:
        diffs = [i for i, (c1, c2) in enumerate(zip(code, other_code)) if c1 != c2]
        if len(diffs) == 1:
            position = diffs[0]
            print(code[0:position] + code[position + 1:])
            exit()

