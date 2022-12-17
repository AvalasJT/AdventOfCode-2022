# Part 1
import heapq
from copy import deepcopy

import time

valves = []
ways = {}
tunnels = {}
parallel_estimates = {}
parallel_calculates = {}

with open('input.txt', 'r') as f:
    for l in f:
        if 'tunnels' in l: valve, tun = l.strip().split('; tunnels lead to valves ')
        else: valve, tun = l.strip().split('; tunnel leads to valve ')
        valve = valve.replace('Valve ', '').split(' has flow rate=')
        tun = tun.split(', ')
        valves.append([valve[0], int(valve[1]), 'off'])
        if not valve[0] in tunnels: tunnels[valve[0]] = tun
        for t in tun:
            if not (valve[0], t) in ways: ways[(valve[0], t)] = 1
            if not (t, valve[0]) in ways: ways[(t, valve[0])] = 1

def get_way(a, b): # Mini A*
    if (a,b) in ways: return ways[(a,b)]
    
    def expand_open_list(current):
        for x in tunnels[current]:
            if x in closed_list:
                continue # Knoten war schon abgeschlossen oder kann nicht erreicht werden
            
            new_g = closed_list[current][0] + 1 # Kosten sind immer Kosten bis jetzt +1
            if x in open_list and open_list[x][0] <= new_g:
                continue # Knoten ist bereits in der open list und gleich gut oder besser
                
            open_list[x] = [new_g, current]   # update or add open_list Eintrag mit neuem g-Wert und Vorgänger
            heapq.heappush(heap, [new_g, x])    # update heap mit g statt f Wert, da kein f-Wert bekannt ist
    
    open_list = {a:[0, None]}   # open list: startkoordinaten keine Kosten bis jetzt (g-Wert) und kein Vorgänger
    closed_list = {}    # closed list: keine Knoten geschlossen
    heap = []   # heap.. magic.. sortierte liste um zu wissen welcher knoten der open_list gerade am vielversprechendsten ist
    heapq.heappush(heap, [0, a]) # in den heap wird der erste Knoten eingefüllt. f-Wert = g + h = kosten bis jetzt + estimate <- darf nie überschätzen
    
    while len(open_list) > 0:
        while len(heap) > 0:
            current = heapq.heappop(heap)[1]
            if current in open_list: break # heap durchgehen bis ein Knoten gefunden ist, der auf der open list steht
        
        closed_list[current] = open_list.pop(current) # current von open list in closed list nehmen (gab keinen kürzeren Pfad mehr)
        
        if current == b: break # Wenn end abschließend in die closed_list kommt -> ende
        expand_open_list(current) # Wenn nicht, dann open list erweitern mit neuen Nachbarknoten
        
    if b in closed_list: # Pfad gefunden -> Länge ausgeben
        current = b
        counter = 0
        while not current == a:
            counter += 1
            current = closed_list[current][1] # vorgänger des aktuellen Knoten
        
        ways[(a,b)] = counter
        ways[(b,a)] = counter
        return counter
    else: # Kein Weg gefunden
        return None


def estimate_parallel_max(curr_valve_state, time1, time2):
    if time1 == time2 == 0: return 0
    valves = deepcopy(curr_valve_state)
    valves = [x for x in valves if x[2] == 'off' and x[1] > 0]   # get the valves which could be opend
    if len(valves) == 0: return 0
    if len(valves) == 1: return valves[-1][1]*(time1 if time1 > time2 else time2)
    valves.sort(key = lambda x: -x[1]) # sort by most promising one
    d_key = str(valves)
    if (d_key, time1, time2) in parallel_estimates: return parallel_estimates[(d_key, time1, time2)]
    if (d_key, time2, time1) in parallel_estimates: return parallel_estimates[(d_key, time2, time1)]
    if time1 == time2 == 1: return valves[-1][1] + valves[-2][1]
    max_gas = 0
    while (time1 > 0 or time2 > 0) and len(valves) > 0:
        if time1 >= time2:
            max_gas += valves[0][1]*time1
            time1 -= 2
        else:
            max_gas += valves[0][1]*time2
            time2 -= 2
        valves = valves[1:]

    parallel_estimates[(d_key, time1, time2)] = max_gas
    return max_gas

def check_skip(d_key, pos1, pos2, time1, time2):
    for i in range(time1, 31):
        for j in range(time2, 31):
            if (d_key, pos1, pos2, i, j) in parallel_calculates: return True
            if (d_key, pos2, pos1, j, i) in parallel_calculates: return True
    return False

def calculate_parallel_max(curr_valve_state, time1, time2, pos1, pos2, gas_so_far, max_gas_so_far):
    if max_gas_so_far[0] > gas_so_far + estimate_parallel_max(curr_valve_state, time1, time2): return 0
    if time1 <= 1 and time2 <= 1: return 0
    valves = deepcopy(curr_valve_state)
    valves = [x for x in valves if x[2] == 'off' and x[1] > 1]   # get the valves which could be opend
    if len(valves) == 0: return 0
    valves.sort(key = lambda x: -x[1]) # sort by most promising one
    d_key = str(valves)
    if (d_key, pos1, pos2, time1, time2) in parallel_calculates: return parallel_calculates[(d_key, pos1, pos2, time1, time2)]
    if (d_key, pos2, pos1, time2, time1) in parallel_calculates: return parallel_calculates[(d_key, pos2, pos1, time2, time1)]
    
    if check_skip(d_key, pos1, pos2, time1, time2): return 0
    
    max_gas = 0
    for valve in valves:
        for x in range(2):
            if x == 1: time1, time2, pos1, pos2 =  time2, time1, pos2, pos1 # test wich switched actors             
            if pos1 == valve[0]:
                valve[2] = 'on'
                gas = (time1-1) * valve[1]
                temp_gas = calculate_parallel_max(valves, time1-1, time2, pos1, pos2, gas_so_far + gas, max_gas_so_far)
                gas += temp_gas
                if gas > max_gas: max_gas = gas
                valve[2] = 'off'
            else:
                way = get_way(valve[0], pos1)
                if time1 <= way: continue
                gas = calculate_parallel_max(valves, time1-way, time2, valve[0], pos2, gas_so_far, max_gas_so_far)
                if gas > max_gas: max_gas = gas
    
    if gas_so_far + max_gas > max_gas_so_far[0]: 
        max_gas_so_far[0] = gas_so_far + max_gas
        print(max_gas_so_far[0])
    parallel_calculates[(d_key, pos1, pos2, time1, time2)] = max_gas
    return max_gas


start_time = time.time()

max_gas_so_far = [0]
print(calculate_parallel_max(valves, 30, 0, 'AA', 'AA', 0, max_gas_so_far))

print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

max_gas_so_far = [0]
print(calculate_parallel_max(valves, 26, 26, 'AA', 'AA', 0, max_gas_so_far))

print("--- %s seconds ---" % (time.time() - start_time))
