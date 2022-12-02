#Part 1 & 2
wins = {'A':'Y', 'B':'Z', 'C':'X'} #Part 1 nomenclature
draw = {'A':'X', 'B':'Y', 'C':'Z'}
lose = {'A':'Z', 'B':'X', 'C':'Y'}
    
def calc_points1(opp, you):
    points = 1 if you == 'X' else (2 if you == 'Y' else 3)
    points += 6 if you == wins[opp] else (3 if you == draw[opp] else 0)
    return points

def calc_points2(opp, out):
    you = wins[opp] if out == 'Z' else (draw[opp] if out == 'Y' else lose[opp])
    return calc_points1(opp, you)

TotalScore1, TotalScore2 = 0, 0
with open('input.txt', 'r') as f:
    for l in f: 
        opp, you_out = l.strip('\n').split()
        TotalScore1 += calc_points1(opp, you_out)
        TotalScore2 += calc_points2(opp, you_out)

print(TotalScore1)
print(TotalScore2)
