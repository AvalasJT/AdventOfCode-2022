# Part 1 + 2
def get_marker(n, sig):
    for pos in range(n, len(sig)+1):
        if len(set(sig[pos-n:pos])) == n: return pos

with open('input.txt', 'r') as f: signal = f.readline().strip('\n')

print(get_marker(4, signal))
print(get_marker(14, signal))
