import os 

# read input
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir,'input.txt'),'r') as f:
    input = f.readlines()



# format input
elf_pairs = [i.replace("\n","") for i in input]

# part 1

# define full overlap counter variable and assign initial value of 0
full_overlap = 0

for elf_pair in elf_pairs:
    # split input per line and identify start-stop values for each elf in each pair
    elf1,elf2 = elf_pair.split(",")
    elf1_start,elf1_stop = elf1.split("-")
    elf1_start = int(elf1_start)
    elf1_stop = int(elf1_stop)
    elf2_start,elf2_stop = elf2.split("-")
    elf2_start = int(elf2_start)
    elf2_stop = int(elf2_stop)

    # if either elf1 start and stop between elf2 start and stop, or elf2 start and stop between elf1 start and stop
    # increment full overlap counter by 1
    if (elf2_start <= elf1_start and elf1_stop <= elf2_stop) or (elf1_start <= elf2_start and elf2_stop <= elf1_stop):
        full_overlap +=1

# print part 1 answer
print(f"There are {full_overlap} cases where one elf's work entirely overlaps the others.")

# part 2

# define partial overlap counter variable and assign initial value of 0
partial_overlap = 0

for elf_pair in elf_pairs:
    # split input per line and identify start-stop values for each elf in each pair
    elf1,elf2 = elf_pair.split(",")
    elf1_start,elf1_stop = elf1.split("-")
    elf1_start = int(elf1_start)
    elf1_stop = int(elf1_stop)
    elf2_start,elf2_stop = elf2.split("-")
    elf2_start = int(elf2_start)
    elf2_stop = int(elf2_stop)

    # if either elf1's start or stop is between elf2's start and stop, or elf2's start or stop between elf1's start and stop
    # increment partial overlap counter by 1
    if (elf1_start <= elf2_start <= elf1_stop) or (elf2_start <= elf1_start <= elf2_stop) or (elf1_start <= elf2_stop <= elf1_stop) or (elf2_start <= elf1_stop <= elf2_stop):
        partial_overlap += 1

# print part 1 answer
print(f"There are {partial_overlap} cases where one elf's work at least partially overlaps the others.")