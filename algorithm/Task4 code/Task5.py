import re
from operator import itemgetter
from math import ceil


def task5(message_filename, is_goal):
    # TODO

    f = open(message_filename)
    text = f.read()

    text = text.replace("\n", " ")
    text = re.sub("[^a-zA-Z ]", "", text)
    text = text.lower()
    text = text.replace(" ", "")

    dictionary = ["A", "E", "N", "O", "S", "T"]
    letter_count = []

    for letter in dictionary:
        count = text.count(letter.lower())
        letter_count.append(count)

    frequency = []
    for i in range(len(dictionary)):
        frequency.append([dictionary[i], letter_count[i]])
    frequency = sorted(frequency, key=itemgetter(1), reverse=True)

    theoretical_goal = list("ETAONS")
    sorted_string = []
    for item in frequency:
        char = item[0]
        sorted_string += char

    # print(sorted_string)
    # print(theoretical_goal)

    counter = 0
    for i in range(len(sorted_string)):

        if sorted_string[i] != theoretical_goal[i]:
            counter += 1

    output = ceil(counter/2)

    if is_goal == True:
        return 0
    else:
        return output


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task5 function
    print(task5('freq_eg1.txt', False))
    print(task5('freq_eg1.txt', True))
    print(task5('freq_eg2.txt', False))
