import os 

# read input (named 'input.txt' in same directory as solution.py file)
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir,'input.txt'),'r') as f:
    input = f.readlines()

# identify break between starting crate arrangements and moves list
for i,line in enumerate(input):
    if line == "\n":
        break

# drop the stack number line
crate_stacks_input = input[0:i-1]

# skip the blank line that was used as the separator and drop trailing new line char
moves_input = input[i+1:]
moves_input = [m.replace("\n","") for m in moves_input]

# create crate_stacks from crate_stacks_input lines
crate_stacks = []
for i,n in enumerate([1,5,9,13,17,21,25,29,33]):
    crate_stacks.append([c[n] for c in crate_stacks_input if c[n] != " "])

# create copies of the initial stack as it needs to be used in parts 1 and 2
crate_stacks_pt1 = crate_stacks.copy()
crate_stacks_pt2 = crate_stacks.copy()

# define function to simpulate moving crates (parts 1 and 2 differentiated by 'part' argument)
def move_crates(stacks,n,from_stack,to_stack,part):
    from_stack -= 1
    to_stack -= 1
    moved_crates = stacks[from_stack][0:n]
    stacks[from_stack] = stacks[from_stack][n:]
    if part == 1: moved_crates.reverse()
    stacks[to_stack] = moved_crates + stacks[to_stack]
    return stacks



# execute all moves (part1)
for move in moves_input:
    move = move.split(" ")
    n = int(move[1])
    start = int(move[3])
    end = int(move[5])
    move_crates(crate_stacks_pt1, n, start, end, part=1)

# extract list of crates on top of stacks, join in single string
crate_toppers_pt1 = "".join([c[0] for c in crate_stacks_pt1])

# print part 1 answer
print(f"Crates on top of stacks (pt1): {crate_toppers_pt1}")


# execute all moves (part2)
for move in moves_input:
    move = move.split(" ")
    n = int(move[1])
    start = int(move[3])
    end = int(move[5])
    move_crates(crate_stacks_pt2, n, start, end, part=2)

# extract list of crates on top of stacks, join in single string
crate_toppers_pt2 = "".join([c[0] for c in crate_stacks_pt2])

# print part 2 answer
print(f"Crates on top of stacks (pt1): {crate_toppers_pt2}")