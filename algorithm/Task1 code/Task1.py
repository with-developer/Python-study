def task1(key, filename, indicator):
    #TODO
        # Open and Read the input file
    f = open(filename, "r")
    txt = f.read()
    
    # Convert strings into a list (including white spaces)
    text_array = list(txt)
    
    # Encryption
    if indicator == "e":
      
      for i in range(0, len(key), 2):
        # eg. Given key: ABCD. AB is a pair and CD is the other pair
        # A and C are the first keys, and B and D are the second keys
        first_key = key[i]
        second_key = key[i+1]

        # Iterate the string list
        for j in range(0,len(text_array)):
          
          # first key = uppercase
          if text_array[j] == first_key:
            text_array[j] = second_key
            
          # first key = lowercase
          elif text_array[j] == first_key.lower():
            text_array[j] = second_key.lower()
            
          # second key = uppercase
          elif text_array[j] == second_key:
            text_array[j] = first_key
          
          # second key = lowercase
          elif text_array[j] == second_key.lower():
            text_array[j] = first_key.lower()
          
          # character not matched to any key
          else:
            continue
            
    # Decryption
    elif indicator == "d":
      
      # decrpytion is in reverse order.
      for i in range(len(key)-1, -1, -2):
        first_key = key[i]
        second_key = key[i-1]
        
        # same process as the encryption
        for j in range(0,len(text_array)):
          if text_array[j] == first_key:
            text_array[j] = second_key
          elif text_array[j] == first_key.lower():
            text_array[j] = second_key.lower()
          elif text_array[j] == second_key:
            text_array[j] = first_key
          elif text_array[j] == second_key.lower():
            text_array[j] = first_key.lower()
          else:
            continue
    
    # return_text will be the output text
    return_txt = ""
    
    # concatenate the character list into one single long string
    for i in range(len(text_array)):
      return_txt += text_array[i]
    
    # close the file as all process are done
    f.close()
    
    # return the encrypted/decrypted string
    return return_txt


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task1 function
    print(task1('AE', 'spain.txt', 'd'))
    print(task1('VFSC', 'ai.txt', 'd'))
    print(task1('ABBC', 'cabs_plain.txt', 'e'))