#Part 1
def contains(r1, r2):
    if (r2[0] >= r1[0] and r2[1] <= r1[1]) or (r1[0] >= r2[0] and r1[1] <= r2[1]):
        return True
    else:
        return False
    
#Part 2
def overlap(r1, r2):
    for r in r1:
        if r >= r2[0] and r <= r2[1]:
            return True
    for r in r2:
        if r >= r1[0] and r <= r1[1]:
            return True
    return False
    
n1, n2 = 0, 0
with open('input.txt', 'r') as f:
    for l in f: 
        r1, r2 = [[int(y) for y in x.split('-')] for x in l.strip().split(',')]
        if contains(r1, r2): 
            n1 += 1
            n2 += 1
        elif overlap(r1, r2): 
            n2 += 1
print(n1, n2)
