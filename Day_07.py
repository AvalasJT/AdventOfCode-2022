# Part 1
class directory:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent_dir = parent
        self.subdirs = []
        self.files = []

    def Add_Subdir(self, subdir_name):
        if not subdir_name in [subdir.name for subdir in self.subdirs]:
            self.subdirs.append(directory(subdir_name, self))
        else:
            print('Subdir', subdir_name, 'already exists in', self.name)

    def Add_File(self, file_name, file_size):
        if not file_name in [file.name for file in self.files]:
            self.files.append(file(file_name, file_size))
        else:
            print('File', file_name, 'already exists in', self.name)
            
    def Get_Subdir(self, subdir_name):
        for subdir in self.subdirs:
            if subdir.name == subdir_name: return subdir
        print('Subdir', subdir_name, 'not found.')
        return self
    
    def Get_Size(self):
        sum_size = 0
        if len(self.subdirs) > 0: sum_size += sum([subdir.Get_Size() for subdir in self.subdirs])
        if len(self.files) > 0: sum_size += sum([file.size for file in self.files])
        return sum_size


class file:
    name = None
    size = 0
    
    def __init__(self, file_name, file_size):
        self.name = file_name
        self.size = file_size


def search_smaller_100k(sdir, sum_s):
    if sdir.Get_Size() <= 100000: sum_s[0] += sdir.Get_Size()
    for d in sdir.subdirs:
        search_smaller_100k(d, sum_s)

# For Part 2
def search_smallest_above(sdir, needed, smallest):
    if needed < sdir.Get_Size() < smallest[0]: smallest[0] = sdir.Get_Size()
    for d in sdir.subdirs:
        search_smallest_above(d, needed, smallest)
    
# Prepare first directory    
root = directory('root')
root.Add_Subdir('/')    
cur_dir = root

with open('input.txt', 'r') as f: 
    for l in f:
        com = l.strip('\n').split()
        if com[0] == '$' and com[1] == 'cd' and com[2] != '..':
            cur_dir = cur_dir.Get_Subdir(com[2])
        elif com[0] == '$' and com[1] == 'cd' and com[2] == '..':
            cur_dir = cur_dir.parent_dir
        elif com[0] == '$' and com[1] == 'ls':
            continue
        elif com[0] == 'dir':
            cur_dir.Add_Subdir(com[1])
        elif com[0].isnumeric() == True:
            cur_dir.Add_File(com[1], int(com[0]))
        else:
            print('Command was not interpreted correctly!')

sum_small = [0] # Pass by reference Python workaround
search_smaller_100k(root, sum_small)
print(sum_small[0])


# Part 2
needed_space = root.Get_Size() - 40000000 if root.Get_Size() > 40000000 else 0
smallest = [root.Get_Size()] # Pass by reference Python workaround
search_smallest_above(root, needed_space, smallest)
print(smallest[0])
