
def task2():
    with open("text3.txt", "w") as file1:
        file1.write("\nThis is a new text file. It has number 3."
                   "\nI had to write it directly in the code. "
                    "\nSo,method write allows to do it.")
        file1.write("\nOne more line")
task2()

def count_statistics(text):
    num_characters = len(text)
    num_lines = text.count("\n")+1
    num_vowels = sum(1 for char in text if char.lower in "aeiouáéíóúýůäëoäëаеиіїоуюяє")
    num_consonants = sum(1 for char in text if char.isalpha() and char.lower() not in "aeiouáéíóúýůäëoäëаеиіїоуюяє")
    num_digits = sum(1 for char in text if char.isdigit())
    return num_characters, num_lines, num_vowels, num_consonants, num_digits

# Open the source text file
with open("text3.txt", "r") as source_file:
    text = source_file.read()


# Calculate statistics
num_characters, num_lines, num_vowels, num_consonants, num_digits = count_statistics(text)

# Open a new file for writing statistics
with open("statistics.txt", "w") as statistics_file:
    statistics_file.write(f"Number of characters:{num_characters}")
    statistics_file.write(f" Number of lines:{num_lines}")
    statistics_file.write("Number of vowels {}\n".format(num_vowels))# from Chat gpt, for older version Python
    statistics_file.write("N Number of consonants {}\n".format(num_consonants))
    statistics_file.write("N Number of  digits {}\n".format(num_digits))

print("Statistics written to statistics.txt file.")

