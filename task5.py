def task5(source_file, target_word):
    with open(source_file, "r") as file:
        lines = file.readlines()

        num_word = sum(1 for line in lines for word in line.split() if word == target_word )
    return num_word


source_file = "text3.txt"
target_word = "write"
word_count = task5(source_file,target_word)

print(f"Number of word '{target_word}' is {word_count}")
