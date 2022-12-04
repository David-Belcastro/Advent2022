score = 0

opp = {'A':1, 'B':2, 'C':3}
pla = {'X':0, 'Y':3, 'Z':6}

def winner(p1, p2):
    if p1 == p2:
        return 3
    if p2 == 3 and p1 == 2 or p2 == 2 and p1 == 1 or p2 == 1 and p1 == 3:
        return 6
    return 0

def selection(p1,p2):
    if p2 == 3:
        return p1
    if p2 == 0:
        if p1 == 1:
            return 3
        else:
            return p1-1
    else:
        if p1 == 3:
            return 1
        else:
            return p1+1

def calculate_score(line):
    opp_play = opp[line[0]]
    pla_play = pla[line[2]]
    return pla_play + selection(opp_play, pla_play)

with open('AdventTwo/input.txt','r') as f:
    for line in f:
        score += calculate_score(line)

print(score)