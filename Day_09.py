# Part 1 + 2
with open('input.txt', 'r') as f: 
    moves = [[l.split()[0], int(l.split()[1])] for l in f.read().strip().split('\n')]

direction = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}

def calc_n_rope(n):
    rope = [(0,0)]*n
    visited = set([(0,0)])
    for [d, n] in moves:
        dx, dy = direction[d]
        for _ in range(n):
            rope[0] = (rope[0][0]+dx, rope[0][1]+dy)
            for i in range(1, len(rope)):
                k1x, k1y = rope[i-1]
                k2x, k2y = rope[i]
                if abs(k1x-k2x) > 1 or abs(k1y-k2y) > 1:
                    k2x += 0 if k1x == k2x else int((k1x-k2x)/abs(k1x-k2x))
                    k2y += 0 if k1y == k2y else int((k1y-k2y)/abs(k1y-k2y))
                    rope[i] = (k2x, k2y)
                if i == len(rope)-1: visited.add(rope[i])
    return len(visited)

print(calc_n_rope(2))
print(calc_n_rope(10))
