# Part 1 + 2
with open('input.txt', 'r') as f:
    commands = f.read().strip().split('\n')

cycle = 1
value = 1
signals = []
interesting_cycles = [20, 60, 100, 140, 180, 220]

screen = ['.']*240

def check():
    global cycle
    if cycle in interesting_cycles:
        signals.append((cycle)*value)
    if abs(value-((cycle-1)%40)) <= 1:
        screen[cycle-1] = '#'
    cycle += 1

for com in commands:
    com = com.split()
    if com[0] == 'noop':
        check()
    else:
        check()
        check()
        value += int(com[1])

print(sum(signals))
for i in range(6):
    print(''.join(screen[i*40:(i+1)*40]))
