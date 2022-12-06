import os 

# read input (named 'input.txt' in same directory as solution.py file)
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir,'input.txt'),'r') as f:
    input = f.readline()

# define a function which will find the first set of 'n' distinct characters in a string
def find_start(signal_str, char_len):
    """
    This function creates a sliding assessment of each sequential set of 'n' characters.
    If the length of the set of these characters is the same as the substring length,
    then the substring contains only unique characters.  The returned integer is the position of 
    the first character after the distint substring (base 1, not base 0).

    param str signal_str: the signal input (puzzle input) as a string
    param int char_len: the length of distinct characters to find

    return: int
    """
    for i in range(char_len,len(signal_str)):
        char_set = signal_str[i-char_len:i]
        if len(set(char_set)) == char_len:
            return i

# find the packet start, which is after the first set of 4 distinct characters in the string
packet_start = find_start(input,4)


# find the message start, which is after the first set of 14 distinct characters in the string
message_start = find_start(input,14)

print(f"Packet Start Position: {packet_start}")

print(f"Message Start Position: {message_start}")