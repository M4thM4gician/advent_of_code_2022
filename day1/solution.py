import os 

# read input
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir,'input.txt'),'r') as f:
    input = f.readlines()

# format input
input = [i.replace("\n","") for i in input]

# convert list input to list of lists (list of elves each with a list of calorie values)
elf_index = 0
elf_calories = []
for i in input:
    if len(elf_calories) != (elf_index+1):
        elf_calories.append(list())
    if i == '':
        elf_index += 1
    else:
        elf_calories[elf_index].append(int(i))

# create list of total calories carried by each elf
sum_elf_calories = [sum(l) for l in elf_calories]

# get the max of the all sums
print(f"Maximum calories carried by 1 elf: {max(sum_elf_calories)}")

# inplace alterations to the list: sort ascending, reverse order, select top 3
sum_elf_calories.sort()
sum_elf_calories.reverse()
sum_elf_calories = sum_elf_calories[0:3]
print(f"Maximum calories carried by 3 elves: {sum(sum_elf_calories)}")
