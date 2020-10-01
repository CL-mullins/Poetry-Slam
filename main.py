import random

def get_file_lines(filename):
    infile = open(filename, 'r') 
    lines = infile.read().splitlines()
    return lines

        

def lines_printed_backwards(lines_list):
    line_length = len(lines_list)
    lines_list.reverse()
    for i in range(line_length):
        print(f"{line_length - i} {lines_list[i]}")

def lines_printed_random(lines_list):
    line_length = len(lines_list)
    for i in range(line_length):
        print(lines_list[random.randint(0,line_length - 1)])


def lines_printed_custom(lines_list):
    #Prints out each line that has the term 'mother, 'ocean, or 'father'
    for line in lines_list:
        if "Ocean" in line or "mother" in line or "father" in line:
            print(line)
        

        


        


lines_list = get_file_lines('SILOV.txt')
print("      ")
lines_printed_backwards(lines_list)
print("      ")
lines_printed_random(lines_list)
print("      ")
lines_printed_custom(lines_list)
print("      ")
