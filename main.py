line_list  = []
infile = open('SILOV.txt', 'r')
print("Name of file: ", infile.name)
Lines = infile.readlines()
#print(line)


def get_file_lines(filename):
    for line in Lines:
        line_list.append(line)
    print(line_list)
        
    #for line in :
     #   return line_list
     #   print(line_list)
     #   print("success")
get_file_lines(infile)



#def lines_printed_backwards(line_list):
   # print

#def lines_printed_random()

#def lines_printed_custom()


#if __name__ == "__main__":
   # lines_printed_backwards(line_list)
    #lines_printed_random(line_list)
    #lines_printed_custom(line_list)