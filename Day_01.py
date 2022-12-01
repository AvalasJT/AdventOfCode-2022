#Part 1
Elves = [[]] #List of one Elv with no calories so far
with open('input.txt', 'r') as f:
    for l in f: 
        if l != "\n": #it's a calorie -> add to last Elv
            Elves[-1].append(int(l))
        else:   #line break -> new Elv
            Elves.append([])

SumCal = []        
for E in Elves:
    SumCal.append(sum(E))

print(max(SumCal))

#Part 2
SumCal.sort()
print(sum(SumCal[-3:]))
