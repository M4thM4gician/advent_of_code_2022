import os 
import string 

alphabet = string.ascii_letters

# read input
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir,'input.txt'),'r') as f:
    input = f.readlines()

# part 1

# format input
input = [i.replace("\n","") for i in input]
priority_list = []
for ruck in input:
    ruck = list(ruck)
    compartment_size = int(len(ruck)/2)
    compartment1 = ruck[0:compartment_size]
    compartment2 = ruck[compartment_size:]
    compartment1 = set(compartment1)
    compartment2 = set(compartment2)

    intersection = compartment1.intersection(compartment2)
    intersection = list(intersection)[0]
    
    priority_list.append(list(alphabet).index(intersection)+1)


print(f"Sum of Priorities (part 1): {sum(priority_list)}")

# part 2
priority_list = []

elf_groups = [input[x-2:x+1] for x in range(2,len(input),3)]
for group in elf_groups:
    ruck1 = set(group[0])
    ruck2 = set(group[1])
    ruck3 = set(group[2])

    badge = list(set.intersection(ruck1,ruck2,ruck3))[0]
    badge_priority = list(alphabet).index(badge)+1
    priority_list.append(badge_priority)

print(f"Sum of Priorities (part 1): {sum(priority_list)}")

print([x for x in range(2,len(input),3)])