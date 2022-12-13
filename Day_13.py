# Part 1
def compare(p1, p2):
    if type(p1) == type(p2) == int:    # beides Integer
        return 'good' if p1 < p2 else ('equal' if p1 == p2 else 'bad')
    
    if type(p1) == type(p2) == list: # beides Listen -> solange elemente vergleichen bis entscheidung 
        if len(p1) == 0:    # left leer
            if len(p2) > 0: # aber right nicht -> good
                return 'good'
            else:               # beide leer -> eqaul
                return 'equal'
        
        if len(p2) == 0:    # left nicht leer, aber right -> bad
            return 'bad'
        
        val = 'equal'
        i = 0
        while val == 'equal' and i < min(len(p1), len(p2)):
            val = compare(p1[i], p2[i])
            i += 1
        
        if not val == 'equal':
            return val
        elif len(p1) < len(p2):
            return 'good'
        elif len(p1) == len(p2):
            return 'equal'
        else:
            return 'bad'
        
    if type(p1) == list: # dann p2 ein int
        return compare(p1, [p2])
    else: # dann p2 eine Liste, aber p1 ein Int
        return compare([p1], p2)           

with open('input.txt', 'r') as f:
    pairs = [[eval(p) for p in pairs.split('\n')] for pairs in f.read().strip().split('\n\n')]
    
index = 0
good_indices = []

for p1, p2 in pairs:
    index += 1
    if compare(p1, p2) == 'good': 
        good_indices.append(index)
    
print(sum(good_indices))


# Part 2
def quicksort(array, low, high):    # basic QuickSort Algorithm
    if low < high:
        pivot_index = divide(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)
        
def divide(array, low, high): 
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if compare(array[j], pivot) in ['good', 'equal']:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
        
packets = [ [[2]], [[6]] ]
for p1, p2 in pairs:
    packets.append(p1)
    packets.append(p2)
    
quicksort(packets, 0, len(packets)-1)
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
