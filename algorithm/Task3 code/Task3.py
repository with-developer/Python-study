import re

def task3(message_filename, dictionary_filename, threshold):
    #TODO
    # Open and read message file
    f = open(message_filename)
    text = f.read()
    
    # eleminate new line characters
    text = text.replace("\n"," ")
    
    # remove all special characters (i.e. non-alphabet characters)
    text = re.sub("[^a-zA-Z ]", "", text)
    
    # convert the message file content into a list
    text_array = text.split()

    # open and read the dictionary
    df = open(dictionary_filename, "r")
    words = df.read()
    
    # count the number of words that are found in the given dictionary
    counter = 0
    
    # for each word of the given text
    for s in text_array:
      
      # try to find the word in the dictionary
      for word in words.split():
        
        # if a matched word is found, increment the counter by one
        if s.lower() == word:
          counter += 1
    
    # calculate the percentage of correctness to 2 decimal places
    percentage = '{:.2f}'.format(round(float(counter / len(text_array)) * 100, 2))
    
    # boolean value for validity
    is_valid = False
    
    # check if the calculated percentage is greater or equal to the threshold
    if float(percentage) >= float(threshold):
      
      # if so, set validity to true
      is_valid = True
    
    # format the text to be returned
    return_text = "{}\n{}".format(is_valid, percentage)
    
    # return the output text
    return return_text


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task3 function
    print(task3('jingle_bells.txt', 'dict_xmas.txt', 90))
    print(task3('fruit_ode.txt', 'dict_fruit.txt', 80))
    print(task3('amazing_poetry.txt', 'common_words.txt', 95))