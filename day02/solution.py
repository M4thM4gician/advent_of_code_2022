import os 

# read input
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir,'input.txt'),'r') as f:
    input = f.readlines()

# format input
input = [i.replace("\n","") for i in input]

## Part 1 Reference
# first column is your opponents choice
# second column is your recommended choice
# A = Rock
# B = Paper
# C = Scissors
# X = Rock
# Y = Paper
# Z = Scissors

# Scoring
# 0 for loss, 3 for draw, 6 for win
# 1 for choosing rock (X), 2 for choosing paper (Y), 3 for coosing scissors (Z)

total_score = 0

for rps_round in input:
    a, b = rps_round.split(' ')
    # you choose rock
    if b == 'X':
        total_score += 1
        # draw
        if a == 'A':
            total_score += 3
        # loss
        elif a == 'B':
            total_score += 0 
        # win 
        else:
            total_score += 6
    # you choose paper
    elif b == 'Y':
        total_score += 2
        # win
        if a == 'A':
            total_score += 6
        # draw 
        elif a == 'B':
            total_score += 3
        # loss
        else:
            total_score += 0
    # you choose scissors
    else:
        total_score += 3
        # loss
        if a == 'A':
            total_score += 0
        # win
        elif a == 'B':
            total_score += 6
        # draw
        else:
            total_score += 3

print(f"Part 1 Total Score: {total_score}")


## Part 2 Reference
# first column is your opponents choice
# second column is the recommended outcome
# A = Rock
# B = Paper
# C = Scissors
# X = Lose
# Y = Draw
# Z = Win

# Scoring
# 0 for loss, 3 for draw, 6 for win
# 1 for choosing rock (X), 2 for choosing paper (Y), 3 for coosing scissors (Z)

total_score = 0

for rps_round in input:
    a, b = rps_round.split(' ')
    # you should lose
    if b == 'X':
        total_score += 0
        # pick rock to lose
        if a == 'A':
            total_score += 3
        # pick paper to lose
        elif a == 'B':
            total_score += 1
        # pick scissors to lose
        else:
            total_score += 2
    # you should draw
    elif b == 'Y':
        total_score += 3
        # pick rock to draw
        if a == 'A':
            total_score += 1
        # pick paper to draw
        elif a == 'B':
            total_score += 2
        # pick scissors to draw
        else:
            total_score += 3
    else:
        total_score += 6
        # pick rock to win
        if a == 'A':
            total_score += 2
        # pick paper to win
        elif a == 'B':
            total_score += 3
        # pick scissors to win
        else:
            total_score += 1

print(f"Part 2 Total Score: {total_score}")