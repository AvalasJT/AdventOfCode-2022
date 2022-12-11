# Part 1 + 2
def run_monkey_rounds(n, div_t_f):        
    common_base = 1
    Monkeys = []
    
    class Monkey():
        def __init__(self, ID, items, operation, test_div_number, true_dest, false_dest):
            self.ID = ID
            self.items = items
            self.operation = lambda x: eval(operation)
            self.test_div_number = test_div_number
            self.true_dest = true_dest
            self.false_dest = false_dest
            self.inspected = 0
            
        def test(self, div_t_f, common_base):
            for item in self.items:
                self.inspected += 1
                new = int(self.operation(item) / 3) if div_t_f else int(self.operation(item))
                new = int(new % common_base)
                if new % self.test_div_number == 0:
                    Monkeys[self.true_dest].items.append(new)
                else:
                    Monkeys[self.false_dest].items.append(new)
            self.items = []        
    
    with open('input.txt', 'r') as f:
        for l in f:
            l = l.strip().split()
            if len(l) < 1: continue
            if l[0] == 'Monkey':
                items = [int(x) for x in f.readline().strip()[16:].split(', ')]
                operation = f.readline().strip().replace('old', 'x').replace('Operation: new = ', '')
                test_div_number = int(f.readline().strip().split()[3])
                common_base *= test_div_number
                true_dest = int(f.readline().strip().split()[5])
                false_dest = int(f.readline().strip().split()[5])
                Monkeys.append(Monkey(int(l[1][:-1]), items, operation, test_div_number, true_dest, false_dest))
    
    for _ in range(n):
        for Monkey in Monkeys:
            Monkey.test(div_t_f, common_base)
            
    inspected = [Monkey.inspected for Monkey in Monkeys]
    inspected.sort()
    print(inspected[-1]*inspected[-2])

run_monkey_rounds(20, True)
run_monkey_rounds(10000, False)
