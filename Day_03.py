#Part 1
PriSum = 0
with open('input.txt', 'r') as f:
    for l in f: 
        l = l.strip('\n')
        c1, c2 = l[:int(len(l)/2)], l[int(len(l)/2):]
        for c in c1:
            if c in c2:
                PriSum += ord(c)-96 if ord(c) > 96 else ord(c)-38
                break
print(PriSum)

#Part 2
PriSumBadge = 0
with open('input.txt', 'r') as f:
    while f:
        l1 = f.readline().strip('\n')
        if not l1: break
        l2 = f.readline().strip('\n')
        l3 = f.readline().strip('\n')
        for c1 in l1:
            if c1 in l2:
                if c1 in l3:
                    PriSumBadge += ord(c1)-96 if ord(c1) > 96 else ord(c1)-38
                    break
print(PriSumBadge)
