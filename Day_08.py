# Part 1
import numpy as np

with open('input.txt', 'r') as f: 
    trees = np.asarray([[int(a) for a in line] for line in f.read().strip().split('\n')])

visible = 0
nrows, ncols = np.shape(trees)
for i in range(nrows):
    for j in range(ncols):
        if i in [0, nrows-1] or j in [0, ncols-1]:  # Edges are visible
            visible += 1
            continue
        if trees[i,j] > min(max(trees[i,:j]), max(trees[i,j+1:]), max(trees[:i,j]), max(trees[i+1:,j])):
            visible += 1
            
print(visible)

# Part 2
def sscore(tree, x, y):
    blocks_x = np.argwhere(trees[:,y]>=trees[x,y])
    blocks_y = np.argwhere(trees[x,:]>=trees[x,y])
    
    sc1 = x - max(np.append(blocks_x[blocks_x < x], [0])) #x index - largest blocking index smaller than x index
    sc2 = min(np.append(blocks_x[blocks_x > x], [nrows-1])) - x #smalles blocking index larger than x index - x index

    sc3 = y - max(np.append(blocks_y[blocks_y < y], [0])) #y index - largest blocking index smaller than y index    
    sc4 = min(np.append(blocks_y[blocks_y > y], [ncols-1])) - y #smalles blocking index larger than y index - y index

    return sc1* sc2* sc3* sc4

max_sscore = 0
for i in range(nrows):
    for j in range(ncols):
        s = sscore(trees, i, j)
        if s > max_sscore: max_sscore = s

print(max_sscore)
