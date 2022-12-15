# Part 1
#n_y, n_crop, file = 10, 20, 'input_test.txt' # Test
n_y, n_crop, file = 2000000, 4000000, 'input.txt' # Data

SB = {}
beacons_in_target_row = []
with open(file, 'r') as f:
    for l in f:
        sx, sy, bx, by = l.strip().replace('Sensor at x=', '').replace('y=', '').replace(': closest beacon is at x=', ',').replace('y=', '').split(',')
        SB[(int(sx),int(sy))] = (int(bx),int(by))
        if int(by) == n_y and not [int(bx),int(by)] in beacons_in_target_row: beacons_in_target_row.append([int(bx),int(by)])

def fuse(arr):
    changed = True
    while changed:
        changed = False
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if (arr[i][0]-arr[j][1])*(arr[i][1]-arr[j][0]) <= 0: # the two blocks are overlapping
                    temp1, temp2 = arr[i], arr[j]
                    arr.remove(temp1)
                    arr.remove(temp2)
                    arr.append([min(temp1[0],temp2[0]), max(temp1[1],temp2[1])])
                    
                    changed = True
                    break

            if changed: break

def find_blocks(y):
    blocks = []    
    for s, b in SB.items():
        dist_beacon, dist_row = abs(s[0]-b[0]) + abs(s[1]-b[1]), abs(s[1]-y)
        if dist_beacon < dist_row:
            continue
        blocks.append([s[0] - (dist_beacon - dist_row) , s[0] + (dist_beacon - dist_row)])

    fuse(blocks)
    return blocks

blocks = find_blocks(n_y)
print(sum([x2-x1+1 for (x1,x2) in blocks]) - len(beacons_in_target_row))

#Part 2 ... soo slow :(
def crop(arr, n):
    for i in range(len(arr)):
        for j in [0,1]:
            if arr[i][j] < 0: arr[i][j] = 0
            if arr[i][j] > n: arr[i][j] = n
    fuse(arr)
    
for i in range(n_crop + 1):
    blocks = find_blocks(i)
    crop(blocks, n_crop)
    if len(blocks) > 1:
        blocks.sort()
        print((blocks[0][1]+1)*4000000 + i)
        break
