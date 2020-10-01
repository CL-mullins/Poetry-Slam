
line_list  = []
infile = open('SILOV.txt', encoding='utf-8') 
Lines = infile.readlines()


def get_file_lines(filename):
    for line in Lines:
        line_list.append(line)
    return line_list
        
        
    #for line in :
     #   return line_list
     #   print(line_list)
     #   print("success")

#def lines_printed_backwards(list):
 #   reverse_list = line_list.reverse()
  #  print(reverse_list)
    

#def lines_printed_random()

#def lines_printed_custom()
get_file_lines(infile)
print(line_list)

#if __name__ == "__main__":
   # lines_printed_backwards(line_list)
    #lines_printed_random(line_list)
    #lines_printed_custom(line_list)