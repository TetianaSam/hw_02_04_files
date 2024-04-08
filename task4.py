def task4(source_file):
    with open(source_file, "r") as file:
        max_length= 0
        for line in file:
            line_length = len(line.rstrip())
            if line_length > max_length:
                 max_length =line_length
    return max_length

source_file = "text1.txt"
longest_line = task4(source_file)

print(f"The longest line in the {source_file} is {longest_line}")