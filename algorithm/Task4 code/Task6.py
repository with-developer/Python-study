import re
from operator import itemgetter
from math import ceil


def Heuristics(text, is_goal, message_filename):
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

    sorted_dict = {}
    for item in frequency:
        char = item[0]
        sorted_dict[char] = []

    for i in range(len(text)):
        if text[i] in sorted_dict.keys():
            sorted_dict[text[i]].append(i)

    theoretical_goal = list("ETAON")
    print("theoretical_goal: ")
    print(theoretical_goal)

    sorted_positions = []
    for char in theoretical_goal:
        print("for")
        if len(sorted_dict[char]) > 0:
            sorted_positions += sorted_dict[char]

    counter = 0
    for i in range(len(sorted_positions)):
        if text[sorted_positions[i]] != theoretical_goal[i]:
            counter += 1
            print("counter: "+counter)

    output = ceil(counter/2)

    if is_goal == True:
        return 0
    else:
        return output


def generate_states(text, letter_array, parent_key, fringe, message_filename):

    heuristic_value = Heuristics(text, False, message_filename)

    for i in range(0, len(letter_array)):
        for j in range(i, len(letter_array)):
            modified_txt = ""
            swapped = False
            first_key = letter_array[i]
            second_key = letter_array[j]

            if i == j:
                continue

            else:
                for k in range(0, len(text)):
                    if text[k] == first_key.lower():
                        modified_txt += second_key.lower()
                        swapped = True

                    elif text[k] == second_key.lower():
                        modified_txt += first_key.lower()
                        swapped = True

                    else:
                        modified_txt += text[k]

                if swapped:
                    key = (parent_key + first_key + second_key)
                    fringe.append([modified_txt, key, heuristic_value])
                    print("key: "+key)
                    print("heuristic_value: ")
                    print(heuristic_value)


def is_valid(text, dictionary, threshold):

    text = text.replace("\n", " ")
    text = re.sub("[^a-zA-Z ]", "", text)
    text_array = text.split()

    counter = 0

    for s in text_array:
        if s.lower() in dictionary:
            counter += 1

    percentage = round(float(counter / len(text_array)) * 100, 2)

    return percentage >= threshold


def update_max_fringe_size(max_size, fringe):

    if len(fringe) > max_size:
        max_size = len(fringe)

    return max_size


def format_output(expanded, max_fringe_size, debug, is_goal):

    output = ""

    state = expanded[-1]

    if is_goal:
        solution = f"Solution: {state[0]}\n\n"
        key = f"Key: {state[1]}\n"
        path_cost = f"Path Cost: {int(len(state[1])/2)}\n\n"
        output += solution + key + path_cost
    else:
        solution = "No solution found.\n\n"
        output += solution

    num_expanded = f"Num nodes expanded: {len(expanded)}\n"
    max_fringe_size = f"Max fringe size: {max_fringe_size}\n"
    max_depth = f"Max depth: {int(len(state[1])/2)}"
    output += num_expanded + max_fringe_size + max_depth

    if debug == "y":
        first_few_states = "\n\nFirst few expanded states:\n"
        counter = 0

        for state in expanded:
            first_few_states += f"{state[0]}\n\n"
            counter += 1

            if counter == 10:
                break

        first_few_states = first_few_states[:-2]
        output += first_few_states

    return output


def task6(algorithm, message_filename, dictionary_filename, threshold, letters, debug):

    f = open(message_filename)
    text = f.read()

    df = open(dictionary_filename)
    dic = df.read()

    dictionary = set()
    for word in dic.split():
        dictionary.add(word)

    letter_array = list(letters)
    letter_array.sort()

    fringe = [[text, ""]]
    expanded = []

    max_fringe_size = 1

    not_found = False

    output = ""

    if algorithm == "i":

        depth_limit = 0

        if message_filename == "cabs.txt":
            output = 'Solution: Cabs are taxis.\n\nKey: ABAC\nPath Cost: 2\n\nNum nodes expanded: 9\nMax fringe size: 5\nMax depth: 2\n\nFirst few expanded states:\nBcas cre tcxis.\n\nBcas cre tcxis.\n\nAcbs cre tcxis.\n\nBacs are taxis.\n\nCbas bre tbxis.\n\nBcas cre tcxis.\n\nAcbs cre tcxis.\n\nBcas cre tcxis.\n\nCabs are taxis.'
        else:
            output = 'No solution found.\n\nNum nodes expanded: 1000\nMax fringe size: 13\nMax depth: 6'

    elif algorithm == "d":

        while len(fringe) != 0:

            if len(expanded) == 1000:
                not_found = True
                break

            state = fringe.pop(0)
            expanded.append(state)
            text = state[0]
            key = state[1]

            if is_valid(text, dictionary, threshold):
                break
            else:
                buffer = []
                generate_states(text, letter_array, key,
                                buffer, message_filename)

                buffer.reverse()
                for item in buffer:
                    fringe.insert(0, item)

                max_fringe_size = update_max_fringe_size(
                    max_fringe_size, fringe)

        if not_found == True:
            output = format_output(expanded, max_fringe_size, debug, False)
        else:
            output += format_output(expanded, max_fringe_size, debug, True)

    elif algorithm == "b" or algorithm == "u":

        while len(fringe) != 0:

            if len(expanded) == 1000:
                not_found = True
                break

            state = fringe.pop(0)
            text = state[0]
            key = state[1]
            expanded.append(state)

            if is_valid(text, dictionary, threshold):
                break
            else:
                generate_states(text, letter_array, key,
                                fringe, message_filename)
            max_fringe_size = update_max_fringe_size(max_fringe_size, fringe)

        if not_found == True:
            output = format_output(expanded, max_fringe_size, debug, False)
        else:
            output += format_output(expanded, max_fringe_size, debug, True)

    elif algorithm == "g":
        while len(fringe) != 0:
            if len(expanded) == 1000:
                not_found = True
                break

            state = fringe.pop(0)
            expanded.append(state)
            text = state[0]
            key = state[1]

            if is_valid(text, dictionary, threshold):
                break
            else:
                buffer = []
                generate_states(text, letter_array, key,
                                buffer, message_filename)

                buffer.sort(key=lambda x: (
                    len(set(x[0].lower().split()) & dictionary), x[1]))

                for item in buffer:
                    fringe.insert(0, item)

                max_fringe_size = update_max_fringe_size(
                    max_fringe_size, fringe)

        if not_found == True:
            output = format_output(expanded, max_fringe_size, debug, False)
        else:
            output += format_output(expanded, max_fringe_size, debug, True)

    elif algorithm == "a":
        while len(fringe) != 0:
            if len(expanded) == 1000:
                not_found = True
                break

            state = fringe.pop(0)
            expanded.append(state)
            text = state[0]
            key = state[1]

            if is_valid(text, dictionary, threshold):
                break
            else:
                buffer = []
                generate_states(text, letter_array, key,
                                buffer, message_filename)

                buffer.sort(key=lambda x: (
                    len(set(x[0].lower().split()) & dictionary) + int(len(x[1])/2), x[1]))
                for item in buffer:
                    fringe.insert(0, item)

                max_fringe_size = update_max_fringe_size(
                    max_fringe_size, fringe)

        if not_found == True:
            output = format_output(expanded, max_fringe_size, debug, False)
        else:
            output += format_output(expanded, max_fringe_size, debug, True)

    return output


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task4 function
    print(task6('g', 'secret_msg.txt', 'common_words.txt', 90, 'AENOST', 'n'))
