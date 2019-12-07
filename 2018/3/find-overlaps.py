# guaranteed to be the most efficient method, 100%

CLOTH_LEN = 1000

def get_coords_for_claim(line):
    sections = line.split(' ')
    (x,y) = map(int, sections[2][0:-1].split(','))
    (w,h) = map(int, sections[3].split('x'))
    return [(cloth_x, cloth_y) for cloth_y in range(y, y + h) for cloth_x in range(x, x + w)]

claims = open('input.txt').read().strip().split('\n')
collisions = [[0] * CLOTH_LEN for _ in range(CLOTH_LEN)]

for (x,y) in [coords for sublist in map(get_coords_for_claim, claims) for coords in sublist]:
    collisions[x][y] += 1

num_overlaps = len([n for line in collisions for n in line if n > 1])
print("{} overlaps".format(num_overlaps))

