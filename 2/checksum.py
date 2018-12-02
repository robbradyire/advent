def find_counts(code):
    counts = {}
    for c in code:
        counts[c] = counts[c] + 1 if c in counts else 1
    return counts

twice_count = 0
thrice_count = 0

codes = open("input.txt").read().strip().split('\n')

for code in codes:
    counts = find_counts(code).values()
    if any(count == 2 for count in counts):
        twice_count += 1
    if any(count == 3 for count in counts):
        thrice_count += 1
    
print("Checksum: {}".format(twice_count * thrice_count))

