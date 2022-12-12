import numpy as np
import heapq

with open('input.txt', 'r') as f:
    grid = np.asarray([[char for char in line] for line in f.read().strip().split('\n')])
    
start = tuple(np.argwhere(grid == 'S')[0])
end = tuple(np.argwhere(grid == 'E')[0])

grid[start] = 'a'
grid[end] = 'z'

def find_path_from(start):
    def estimate_dist(coords):  # h-Wert
        dist_xy = abs(end[0] - coords[0]) + abs(end[1] - coords[1])
        dist_hight = ord('z') - ord(grid[coords])
        return dist_xy if dist_xy >= dist_hight else dist_hight
    
    def expand_open_list(current):
        for x,y in [[-1,0], [1, 0], [0, -1], [0, 1]]:
            x += current[0]
            y += current[1]
            if not 0 <= x <= len(grid[:])-1 or not 0 <= y <= len(grid[0])-1:
                continue # bad indices
            if (x,y) in closed_list or ord(grid[x,y])-ord(grid[current]) > 1:
                continue # Knoten war schon abgeschlossen oder kann nicht erreicht werden
            
            new_g = closed_list[current][0] + 1 # Kosten sind immer Kosten bis jetzt +1
            if (x,y) in open_list and open_list[x,y][0] <= new_g:
                continue # Knoten ist bereits in der open list und gleich gut oder besser
                
            new_f = new_g + estimate_dist((x,y))  # neuer estimated f-Wert
            open_list[(x,y)] = [new_g, current]   # update or add open_list Eintrag mit neuem g-Wert und Vorgänger
            heapq.heappush(heap, [new_f, (x,y)])    # update heap - wenn (x,y) schon drinnen stand, dann steht das neue jetzt aber vorher drinnen und er nimmt später immer das erste und wenn das durch ist, verschwindet der knoten aus der open list-> in heap dürfen die alten Werte drinnen bleiben
    
    open_list = {start:[0, None]}   # open list: startkoordinaten keine Kosten bis jetzt (g-Wert) und kein Vorgänger
    closed_list = {}    # closed list: keine Knoten geschlossen
    heap = []   # heap.. magic.. sortierte liste um zu wissen welcher knoten der open_list gerade am vielversprechendsten ist
    heapq.heappush(heap, [estimate_dist(start), start]) # in den heap wird der erste Knoten eingefüllt. f-Wert = g + h = kosten bis jetzt + estimate <- darf nie überschätzen
    
    while len(open_list) > 0:
        while len(heap) > 0:
            current = heapq.heappop(heap)[1]
            if current in open_list: break # heap durchgehen bis ein Knoten gefunden ist, der auf der open list steht
        #if current == end:
            #print('Weg gefunden - noch nicht unbedingt der beste?')
        
        closed_list[current] = open_list.pop(current) # current von open list in closed list nehmen (gab keinen kürzeren Pfad mehr)
        
        if current == end: break # Wenn end abschließend in die closed_list kommt -> ende
        
        expand_open_list(current) # Wenn nicht, dann open list erweitern mit neuen Nachbarknoten
        
    # Ende while: Keine offenen Knoten mehr. Entweder bester Weg gefunden, oder kein Weg.')
    
    if end in closed_list: # Pfad gefunden -> Länge ausgeben
        current = end
        counter = 0
        while not current == start:
            counter += 1
            current = closed_list[current][1] # vorgänger des aktuellen Knoten
            
        return counter
    else: # Kein Weg gefunden
        return None

print(find_path_from(start))

shortest = []
for x,y in np.argwhere(grid == 'a'):
    steps = find_path_from((x,y))
    if not steps == None: shortest.append(find_path_from((x,y)))
print(min(shortest))
