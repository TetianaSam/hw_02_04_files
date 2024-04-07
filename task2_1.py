def task2():
    with open("text3.txt", "w") as file1:
        file1.write("\nThis is a new text file. It has number 3."
                   "\nI had to write it directly in the code. "
                    "\nSo,method write allows to do it.")
        file1.write("\nOne more line")
task2()

def count_statistics(text):
    num_characters = len(text)
    num_lines = text.count("\n") + 1
    num_vowels = sum(1 for char in text if char.lower() in "aeiouáéíóúýůäëoäëаеиіїоуюяє") #char.lower() перетворює усі літери в нижній регістр
    num_consonants = sum(1 for char in text if char.isalpha() and char.lower() not in "aeiouáéíóúýůäëoäëаеиіїоуюяє") #if char.isalpha() чи є знак літерою
    num_digits = sum(1 for char in text if char.isdigit()) #if char.isdigit() чи є знак цифрою
    return num_characters, num_lines, num_vowels, num_consonants, num_digits

# Open the source text file
with open("text3.txt", "r") as source_file:  # прочитати файл
    text = source_file.read()

# Calculate statistics
num_characters, num_lines, num_vowels, num_consonants, num_digits = count_statistics(text)  # вирахувати статистику і яку саме статистику

# Open a new file for writing statistics
with open("statistics.txt", "w") as statistics_file:  # відкрити новий файл а написати там, що саме написати розписано нижче
    statistics_file.write(f"Number of characters: {num_characters}\n")
    statistics_file.write(f"Number of lines: {num_lines}\n")
    statistics_file.write(f"Number of vowels: {num_vowels}\n")
    statistics_file.write(f"Number of consonants: {num_consonants}\n")
    statistics_file.write(f"Number of digits: {num_digits}\n")

print("Statistics written to statistics.txt file.")  # вивести повідомлення на екран