# Part 1
import numpy as np

with open('input_test.txt', 'r') as f:
    rocklines = [[[int(x) for x in point.split(',')] for point in line.split(' -> ')] for line in f.read().strip().split('\n')]
    
x, y = [500], [0]   # starting point
for line in rocklines: 
    for point in line: 
        x.append(point[0])
        y.append(point[1])
x_max, x_min, y_max, y_min = max(x), min(x), max(y), min(y)
        
cave = np.empty((x_max - x_min + 3, y_max - y_min + 2), dtype=str) # add a line left and right and one below the last rock (+1 each for start and end is included)
cave.fill('.')
cave[500 - x_min +1, 0 - y_min] = '+' # starting point

for line in rocklines:
    for i in range(len(line)-1):
        x1, x2 = line[i][0] - x_min + 1, line[i+1][0] - x_min + 1
        if x1 > x2: x1, x2 = x2, x1
        y1, y2 = line[i][1] - y_min, line[i+1][1] - y_min
        if y1 > y2: y1, y2 = y2, y1

        cave[x1:x2+1, y1:y2+1] = '#'

def sand():
    global x_min
    global cave           
    y_abyss = np.shape(cave)[1] - 1
    addcol = ['.']*(np.shape(cave)[1]-1)
    addcol.append(cave[-1,-1])

    while True: # not abyss and not starting point
        curx, cury = 500 - x_min +1, 0 - y_min
        while True: # sand is still in motion
            if curx == 0:
                cave = np.vstack((addcol, cave))
                x_min -= 1
                curx += 1
            if curx == np.shape(cave)[0] - 1:
                cave = np.vstack((cave, addcol))
                
            if cave[curx, cury + 1] == '.':
                cury += 1
                if cury == y_abyss: break
                continue
            if cave[curx-1, cury + 1] == '.':
                curx -= 1
                cury += 1
                if cury == y_abyss: break
                continue
            if cave[curx+1, cury + 1] == '.':
                curx += 1
                cury += 1
                if cury == y_abyss: break
                continue
            
            cave[curx, cury] = 'o'
            break
            
        if cury == y_abyss: break
        if (curx, cury) == (500 - x_min +1, 0 - y_min): break
        
    return sum(sum(cave == 'o'))
    
print(sand())

# Part 2
cave = np.hstack((cave, np.transpose([['#']*np.shape(cave)[0]])))
print(sand())
