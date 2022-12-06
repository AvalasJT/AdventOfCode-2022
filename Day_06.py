# Part 1 
def get_marker(n):
    pos = n
    while True:
        if len(set(signal[pos-n:pos])) == n: break
        pos += 1
    return pos

with open('input.txt', 'r') as f: signal = f.readline().strip('\n')

print(get_marker(4))

# Part 2
print(get_marker(14))
