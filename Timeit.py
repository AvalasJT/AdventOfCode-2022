import timeit
import os, sys

Day = '02'  #all solutions are in subfolders and are named like "/Day_01/Day_01.py"
rounds = 10

os.chdir('./Day_'+Day) #change working directory, otherwise input.txt is not found

temp = sys.stdout
sys.stdout = open(os.devnull, 'w') #block prints

result = timeit.timeit(stmt=open("./Day_"+Day+".py").read(), globals=globals(), number=rounds)

sys.stdout = temp #enable printing
print('Day ' + Day + ' Avarage execution time: \n', result/rounds)
