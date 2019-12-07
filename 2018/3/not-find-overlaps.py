# guaranteed to be the most efficient method, 100%

CLOTH_LEN = 1000

def get_coords_for_claim(line):
    sections = line.split(' ')
    id = int(sections[0][1:])
    (x,y) = map(int, sections[2][0:-1].split(','))
    (w,h) = map(int, sections[3].split('x'))
    return [(id, cloth_x, cloth_y) for cloth_y in range(y, y + h) for cloth_x in range(x, x + w)]

claims = open('input.txt').read().strip().split('\n')
collisions = [[None] * CLOTH_LEN for _ in range(CLOTH_LEN)]

invalid_ids = set()

ids_and_coords = [ids_and_coords for sublist in map(get_coords_for_claim, claims) for ids_and_coords in sublist]

for (id,x,y) in ids_and_coords:
    last_id = collisions[x][y]
    collisions[x][y] = id

    if last_id is not None and last_id != id:
        invalid_ids.add(id)
        invalid_ids.add(last_id)

for (id,_,_) in ids_and_coords:
    if id not in invalid_ids:
        print("Got it: {}".format(id))
        exit()

