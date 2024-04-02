
#Task1
def is_mismatched_lines(file1_name,file2_name):
    #print("Reading lines")
    file1_name= "text1.txt"
    file2_name = "text2.txt"
    file1 = open(file1_name, "r")
    file1_lines = file1.readlines()

    file2 = open(file2_name, "r")
    file2_lines = file2.readlines()

    print("Lines from", file1_name,":", file1_lines)
    print("Lines from", file2_name,":", file2_lines)
    for line_num, (line1, line2) in enumerate(zip(file1_lines,file2_lines), start =1):
        if line1 != line2:
            print(f"Mismatch at line {line_num}:")
            print(f"{file1_name}: {line1.strip()}")
            print(f"{file2_name}: {line2.strip()}")

    file1.close()
    file2.close()
f1_name = "text1.txt"
f2_name = "text2.txt"
is_mismatched_lines(f1_name, f2_name)


