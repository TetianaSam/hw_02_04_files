def task6(source_file, target_word,replacement_word):
    with open(source_file, "r") as file:
        content = file.read()

    # Perform the replacement
    new_content = content.replace(target_word, replacement_word)


    with open(source_file, "w") as file:
        file.write(new_content)


source_file = "text1.txt"
target_word = "sequence"
replacement_word = "SEQUENCE"
task6(source_file, target_word, replacement_word)