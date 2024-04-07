def task3(source_file, new_file):
    with open(source_file, "r") as s_file:
        lines = s_file.readlines()[:-1] # прочитає всі рядки, крім останнього


    with open(new_file,"w") as n_file:
        n_file.writelines(lines)

source_file = "statistics.txt"
new_file ="new file.txt"
task3(source_file,new_file)
