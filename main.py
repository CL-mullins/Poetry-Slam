
line_list  = []
infile = open('SILOV.txt', 'r') 
Lines = infile.read().splitlines()
print(Lines)


def get_file_lines(filename):
    for line in Lines:
        line_list.append(line)
    return line_list

        
      
    #for line in :
     #   return line_list
     #   print(line_list)
     #   print("success")

def lines_printed_backwards(list):
    for line, a in enumerate(list):
        print("{0}. {1}".format(line,a))
    #    line_list.insert(1 * line)
    #print(list.reverse)
    
    

#def lines_printed_random()

#def lines_printed_custom()
get_file_lines(infile)
for line in line_list:
    print(line)

#lines_printed_backwards(line_list)

#if __name__ == "__main__":
   # lines_printed_backwards(line_list)
    #lines_printed_random(line_list)
    #lines_printed_custom(line_list)