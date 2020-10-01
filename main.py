import random

def get_file_lines(filename):
    infile = open(filename, 'r') 
    lines = infile.read().splitlines()
    #for line in lines:
     #   line_list.append(line)
    return lines

        
      
    #for line in :
     #   return line_list
     #   print(line_list)
     #   print("success")

#num_list = list(enumerate(line_list,1))
#TODO: Give each line a line number
def lines_printed_backwards(lines_list):
    line_length = len(lines_list)
    lines_list.reverse()
    for i in range(line_length):
        print(f"{line_length - i} {lines_list[i]}")

def lines_printed_random(lines_list):
    line_length = len(lines_list)
    for i in range(line_length):
        print(lines_list[random.randint(0,line_length)])
        

        


        

    #    line_list.insert(1 * line)
    #print(list.reverse)
    
#num_list.reverse()   

#def lines_printed_random()

#def lines_printed_custom()

#for line in line_list:
 #   print(line)
lines_list = get_file_lines('SILOV.txt')
#print(lines_list)
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)

#lines_printed_backwards(line_list)
#lines_printed_backwards(line_list)
#lines_printed_backwards(line_list)

#lines_printed_backwards(line_list)

#if __name__ == "__main__":
   # lines_printed_backwards(line_list)
    #lines_printed_random(line_list)
    #lines_printed_custom(line_list)
