def task2(filename, letters):
    #TODO
    
    # Open and read the input file
    f = open(filename, "r")
    txt = f.read()
    
    # convert the input file content into a list
    txt_array = list(txt)
    
    # convert "letters" string into a list and sort the list in the alphabetical order
    letter_array = list(letters)
    letter_array.sort()
    
    # the text to be returned at the end of the program
    return_txt = ""
    
    # path cost (i.e. the number of letter swaps)
    path_cost = 0
    
    # iterate the sorted letters array using double loop
    # eg) ABZD -> AB -> AD -> AZ -> BD -> BZ -> DZ
    for i in range(0, len(letter_array)):
      for j in range(i, len(letter_array)):
        
        # skip and do nothing when letters are same (eg. A <-> A, B <-> B) 
        if i == j:
          continue
        
        # swap letters on the original texts the program is given
        else:
          
          # eg. Given key: ABCD. AB is a pair and CD is the other pair
          # A and C are the first keys, and B and D are the second keys
          first_key = letter_array[i]
          second_key = letter_array[j]
          
          # boolean flag for marking if any of letters are swapped
          # True = swap happened, False = no swaps
          swapped = False
          
          # modified(swapped) text
          modified_txt = ""
          
          # iterate each character in the original texts
          for k in range(0, len(txt_array)):
            
            # if found character to be swapped, swap the letters and mark it swapped
            # append to the modified text
            if txt_array[k] == first_key:
              modified_txt += second_key
              swapped = True
            
            elif txt_array[k] == first_key.lower():
              modified_txt += second_key.lower()
              swapped = True

            elif txt_array[k] == second_key:
              modified_txt += first_key
              swapped = True

            elif txt_array[k] == second_key.lower():
              modified_txt += first_key.lower()
              swapped = True
            
            # char does not match to any key
            else:
              # reached the end of the text
              if txt_array[k] == ".":
                
                # if no swap happens, do not append modified text to the return_txt
                # then move on to the next letter pair
                if swapped == False:
                  continue
                  
                # if swapped, add new line char at the end of the modified text
                # append the modified text to the return_txt
                # increment path_cost
                else:
                  modified_txt += ".\n\n"
                  return_txt += modified_txt
                  path_cost += 1
              
              # append the char to modified text
              else:
                modified_txt += txt_array[k]
                
    
    # if the path cost == 0, no swap happens.
    # return only the path cost, which is 0.
    if path_cost == 0:
      return_txt = "0"
      
    # if swapped, return the path cost and all of the swapped texts
    else:
      return_txt = str(path_cost)+ "\n" + return_txt[:-2]
    
    # close the file as all process are done
    f.close()
    
    # return the solution
    return return_txt
if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task2 function
    print(task2('spain.txt', 'ABE'))
    print(task2('ai.txt', 'XZ'))
    print(task2('cabs.txt', 'ABZD'))