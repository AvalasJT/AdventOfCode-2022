# Part 1 
n_stacks = 9 # dynamisch auslesen?

stacks1 = [[] for x in range(n_stacks)] # deque statt list.. schneller für Part 1 aber unpraktisch für Part 2
moves = []
with open('input.txt', 'r') as f:
    for l in f:
        if l == '\n': continue # seperator between stack graph and moves
        if not l[0] =='m': # still in stack area            
            row = list(l.strip('\n'))
            for i,s in enumerate(stacks1):
                if not row[1+4*i] == ' ':
                    s.insert(0, row[1+4*i])
        else: # moves
            row = l.strip('\n').split()
            moves.append([int(row[x]) for x in [1, 3, 5]])
            
stacks2 = [list(x) for x in stacks1] # deep copy a list for Part 2
for n, fr, to in moves:
    for i in range(n):
        stacks1[to-1].append(stacks1[fr-1].pop())
        
print(''.join([stacks1[x][-1] for x in range(n_stacks)]))

# Part 2
for n, fr, to in moves:
    stacks2[to-1].extend(stacks2[fr-1][-n:])
    stacks2[fr-1] = stacks2[fr-1][:-n]
        
print(''.join([stacks2[x][-1] for x in range(n_stacks)]))
